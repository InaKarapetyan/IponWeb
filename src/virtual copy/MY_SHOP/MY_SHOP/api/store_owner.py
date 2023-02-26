import json
from django.views.generic import View
from django.http import HttpResponse
from MY_SHOP.polls.models import *
from django.core import serializers


#________________________________

class StoreOwnerView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self,request):
        categories = StoreOwner.objects.all()
        data = []
        for category in categories:
            data.append({"user": category.user.username,
                         "avatar": category.avatar,
                         "registered_at": category.registered_at})
            
        data = serializers.serialize('json', categories, fields=('user', 'avatar', "registered_at", 'customer', 'total_price'))
        return self.data_status(data)
    

#________________________________


    def post(self, request):
        data = json.loads(request.body)
        user_id = data['user_id']
        if user_id:
            user = User.objects.get(id=user_id)
            owner = StoreOwner.objects.create(user=user)
            owner.save()
            return self.data_status(data)
        else:
            return "Missing user_id"


#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return StoreOwnerView.get_single(request,id)
        if request.method =="DELETE":
            return StoreOwnerView.delete(request,id)
        if request.method =="PATCH":
            return StoreOwnerView.edit(request,id) 
        
#________________________________


    @staticmethod
    def get_single(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except StoreOwner.DoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        data = {"id": owner.id,
                "user": owner.user.id,
                "avatar": owner.avatar.url if owner.avatar else None,
                "registered_at": owner.registered_at}
        
        return StoreOwnerView.data_status(data)

#________________________________

    @staticmethod
    def delete(request, id):
        try:
            category = StoreOwner.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return StoreOwnerView.data_status()


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreOwner.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "user" in data:
            category.user = data['user']
        if "avatar" in data:
            category.avatar = data['avatar']
        if "registered_at" in data:
            category.registered_at = data['registered_at']
        category.save()
        return StoreOwnerView.data_status(data)