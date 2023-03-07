from __future__ import absolute_import
import json
from django.views.generic import View
from django.http import HttpResponse
from MY_SHOP.polls.models import *
from django.core import serializers
from ..celery import app
from ..tasks import *





#________________________________

class MyBugView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self,request):
        send_feedback_email_task.delay()
        categories = MyBug.objects.all()
        data = []
        for category in categories:
            data.append({"items": category.items,
                         "customer": category.customer.id,
                         "total_price": str(category.total_price)})
            data = serializers.serialize('json', categories, fields=('items', 'customer', 'total_price'))
        return HttpResponse(data, content_type='application/json')



#________________________________
    
    def post(self, request):
        data = json.loads(request.body)
        customer_data = data.get('customer', {})

        # Create a new customer if provided in the request data
        if customer_data:
            customer = Customer.objects.create(**customer_data)
        else:
            customer = None

        # Create a new MyBug instance
        mybug = MyBug.objects.create(customer=customer)

        # Add items to the MyBug instance if provided in the request data
        items_data = data.get('items', [])
        for item_data in items_data:
            item = Item.objects.create(**item_data)
            mybug.items.add(item)

        # Update the total price of the MyBug instance
        mybug.total_price = mybug.calculate_total_price(mybug.items.all())
        mybug.save()

        return self.data_status(data)


#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return MyBugView.get_single(request,id)
        if request.method =="DELETE":
            return MyBugView.delete(request,id)
        if request.method =="PATCH":
            return MyBugView.edit(request,id) 
        
#________________________________


    @staticmethod
    def get_single(request, id):
        try:
            mybug = MyBug.objects.get(id=id)
        except FileExistsError:
                return HttpResponse({"status": "obj_not_found"})
        # Get a list of item data dictionaries for each item in the MyBug instance
        item_data = [{"id": item.id,  "price": str(item.price)} for item in mybug.items.all()]

        # Get the customer data dictionary for the MyBug instance's associated customer
        customer_data = {"id": mybug.customer.id}

        # Construct the response dictionary with the MyBug instance data and related objects
        response_data = {"id": mybug.id,  "total_price": str(mybug.total_price), "items": item_data, "customer": customer_data}

        return MyBugView.data_status(response_data)



#________________________________

    @staticmethod
    def delete(request, id):
        try:
            category = MyBug.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return MyBugView.data_status()


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = MyBug.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "items" in data:
        # Clear the existing items for the MyBug instance
            category.items.clear()
            for item_id in data['items']:
                try:
                    item = Item.objects.get(id=item_id)
                except Item.DoesNotExist:
                    return HttpResponse({"status": "item_not_found"})
                category.items.add(item)
        category.total_price = category.calculate_total_price(category.items.all())
        category.save()
        return MyBugView.data_status(data)