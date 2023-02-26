import json
from django.views.generic import View
from django.http import HttpResponse
from MY_SHOP.polls.models import *

#DONE

#________________________________

class StoreView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self,request):
        categories = Store.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name,
                         "owner":category.owner.id,
                         "store_category": category.store_category.id})
        
        return self.data_status(data)
    

#________________________________

    def post(self, request):
        data = json.loads(request.body)
        owner_id = data['owner_id']
        category_id = data['category_id']
        name = data['name']
        owner = StoreOwner.objects.get(id=owner_id)
        category = StoreCategory.objects.get(id=category_id)
        store = Store.objects.create(name=name, owner=owner, store_category=category)
        store.save()
        return self.data_status(data)
        

#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return StoreView.get_single(request,id)
        if request.method =="DELETE":
            return StoreView.delete(request,id)
        if request.method =="PATCH":
            return StoreView.edit(request,id) 
        
#________________________________


    @staticmethod
    def get_single(request,id):
        try:
            category = Store.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        
        return StoreView.data_status({
            "id": category.id,
            "name": category.name,
            "owner_id": category.owner.id,
            "owner_name": category.owner.name,
            "category_id": category.store_category.id,
            "category_name": category.store_category.name,
        })


#________________________________

    @staticmethod
    def delete(request, id):
        try:
            category = Store.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return StoreView.data_status()


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Store.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        if "owner_id" in data:
            try:
                owner = StoreOwner.objects.get(id=data['owner_id'])
            except StoreOwner.DoesNotExist:
                return HttpResponse("Owner not found", status=400)
            category.owner = owner
        if "store_category_id" in data:
            try:
                category = StoreCategory.objects.get(id=data['store_category_id'])
            except StoreCategory.DoesNotExist:
                return HttpResponse("Category not found", status=400)
            category.store_category = category
        category.save()
        return StoreView.data_status(data)