import json
from django.views.generic import View
from django.http import HttpResponse
from MY_SHOP.polls.models import *



#________________________________

class ItemCategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    
    def get(self,request):
        categories = ItemCategory.objects.all()
        data = []
        for category in categories:
            data.append({"Name": category.name, 
                         "Picture": category.picture.url})
        
        return self.data_status(data)
    

#________________________________
    
    def post(self, request):
        data = json.loads(request.body)
        name = data.get("name")
        picture = request.FILES.get("picture")
        category = ItemCategory.objects.create(name=name, picture=picture)
        category.save()
        return self.data_status(data)
#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return ItemCategoryView.get_single(request,id)
        if request.method =="DELETE":
            return ItemCategoryView.delete(request,id)
        if request.method =="PATCH":
            return ItemCategoryView.edit(request,id) 
        
#________________________________


    @staticmethod
    def get_single(request,id):
        try:
            category = ItemCategory.objects.get(id=id)
        except FileExistsError:
            return HttpResponse({"status": "obj_not_found"})
        category_data = {"id": category.id, "name": category.name}
        if category.picture:
            category_data["picture_url"] = category.picture.url
        return ItemCategoryView.data_status({"id": category.id, "name": category.name, "picture_url": category.picture.url })


#________________________________

    @staticmethod
    def delete(request, id):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return ItemCategoryView.data_status(data)


#________________________________

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = ItemCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        if request.FILES.get("picture"):
            category.picture = request.FILES.get("picture")
        category.save()
        return ItemCategoryView.data_status(data)