import json
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
from MY_SHOP.polls.models import *
from decimal import Decimal


#________________________________

class ItemView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self,request):
        items = Item.objects.all()
        data = []
        for item in items:
            data.append( {"id": item.id,
            "name": item.name,
            "category": item.category.name,
            "price": str(item.price),
            "quantity": str(item.quantity),
            "info": item.info,
            "picture_url": item.picture.url if item.picture else None})
        
        return self.data_status(data)
    

#________________________________
    
    @staticmethod
    def post(self, request):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=data['category_id'])
            store = Store.objects.get(id=data['store_id'])
        except (ItemCategory.DoesNotExist, Store.DoesNotExist):
            return JsonResponse({"status": "obj_not_found"}, status=404)

        item = Item(name=data['name'], category=category, store=store, price=data['price'], quantity=data['quantity'], info=data['info'])
        if request.FILES.get("picture"):
            item.picture = request.FILES.get("picture")
        item.save()
        return self.data_status(data)


#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return ItemView.get_single(request,id)
        if request.method =="DELETE":
            return ItemView.delete(request,id)
        if request.method =="PATCH":
            return ItemView.edit(request,id) 
        
#________________________________

    @staticmethod
    def get_single(request, id):
        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            return JsonResponse({"status": "obj_not_found"}, status=404)
        
        item_data = {
            "id": item.id,
            "name": item.name,
            "category": item.category.name,
            "price": str(item.price),
            "quantity": str(item.quantity),
            "info": item.info,
            "picture_url": item.picture.url if item.picture else None
        }
        
        return ItemView.data_status(item_data)

#________________________________

    @staticmethod
    def delete(request, id):
        try:
            category = Item.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return ItemView.ok_status()


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            item = Item.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        if "category" in data:
            category_name = data['category']
            category = ItemCategory.objects.filter(name=category_name).first()
            if category:
                item.category = category
        if "price" in data:
            item.price = Decimal(data['price'])
        if "quantity" in data:
            item.quantity = Decimal(data['quantity'])
        if "info" in data:
            item.info = data['info']
        if "picture" in request.FILES:
            item.picture = request.FILES['picture']
        item.save()
        return ItemView.data_status(data)
        
    


        
