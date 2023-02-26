import json
from django.views.generic import View
from django.http import HttpResponse
from MY_SHOP.polls.models import *
from django.http import JsonResponse
from django.core import serializers


#________________________________

class PurchaseView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self, request):
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append({
                "id": purchase.id,
                "items": [item.id for item in purchase.items.all()],
                "buy_time": purchase.buy_time,
                "customer": purchase.customer.id,
                "total_price": str(purchase.total_price),
            })
        data = serializers.serialize('json', purchases, fields=('id', 'items', "buy_time", 'customer', 'total_price'))
        return self.data_status(data)
    

#________________________________

    def post(self, request):
        data = json.loads(request.body)
        customer = Customer.objects.get(id=data['customer_id'])
        purchase = Purchase.objects.create(customer=customer)
        item_ids = data['item_ids']
        for item_id in item_ids:
            item = Item.objects.get(id=item_id)
            purchase.items.add(item)
        return HttpResponse('Purchase created successfully')
    

#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return PurchaseView.get_single(request,id)
        if request.method =="DELETE":
            return PurchaseView.delete(request,id)
        if request.method =="PATCH":
            return PurchaseView.edit(request,id) 
        
#________________________________


    @staticmethod
    def get_single(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except Purchase.DoesNotExist:
            return JsonResponse({"status": "obj_not_found"})
        
        data = {
            "id": purchase.id,
            "items": [item.name for item in purchase.items.all()],
            "buy_time": purchase.buy_time,
            "customer": purchase.customer.name,
            "total_price": purchase.calculate_total_price,
        }
        return JsonResponse(data)


#________________________________

    @staticmethod
    def delete(request, id):
        try:
            category = Purchase.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return PurchaseView.data_status()


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Purchase.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return PurchaseView.data_status(data)