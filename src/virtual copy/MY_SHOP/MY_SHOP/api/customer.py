import json
from django.views.generic import View
from django.http import HttpResponse
from MY_SHOP.polls.models import *
from django.http import JsonResponse


#________________________________

class CustomerView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self,request):
        categories = Customer.objects.all()
        data = []
        for category in categories:
            data.append({"User": category.user.id,
                         "Avatar": category.avatar.url})
            
        return self.data_status(data)

#________________________________
    
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        avatar = data['avatar']
        registered_at = data ['registered_at']
        customer = Customer.objects.create(user=user, avatar=avatar, registered_at = registered_at)
        customer.save()
        return self.data_status(data)


#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return CustomerView.get_single(request,id)
        if request.method =="DELETE":
            return CustomerView.delete(request,id)
        if request.method =="PATCH":
            return CustomerView.edit(request,id) 
        
#________________________________



    @staticmethod
    def get_single(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return HttpResponse({"status": "obj_not_found"}, status=404)
        
        data = {
            "id": customer.id,
            "user": customer.user.id,
            "avatar": customer.avatar.url,
            "registered_at": customer.registered_at.isoformat()
        }
        
        return JsonResponse(data)





#________________________________

    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        
        customer.delete()
        return HttpResponse({"status": "obj_deleted"})


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = Customer.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "user" in data:
            category.user = data['user']
        if "avatar" in data:
            avatar = data.get("avatar")
            category.avatar = avatar
        category.save()
        return CustomerView.data_status(data)
