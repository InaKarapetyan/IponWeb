import json
from django.views.generic import View
from django.http import HttpResponse
from ..polls.models import StoreCategory
from django.core import serializers



#________________________________

class StoreCategoryView(View):
    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps({"data": data, "status": "ok"}),
            content_type = "application/json"
        )

#________________________________
    

    def get(self, request):
        categories = StoreCategory.objects.all()
        data = []
        if not categories:
            return self.data_status({"message": "No categories found"})
        for category in categories:
            data.append({
                "name": category.name,
                "picture": category.picture.url,
                "pub_date": category.pub_date,
            })
        data = serializers.serialize('json', categories, fields=('name', 'picture', 'pub_date'))
        return HttpResponse(data, content_type='application/json')


    

#________________________________

    def post(self,request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(name=data['name'])
        category.save()
        return self.data_status

#________________________________

    @staticmethod
    def check_view(request,id):
        if request.method =="GET":
            return StoreCategoryView.get_single(request,id)
        if request.method =="DELETE":
            return StoreCategoryView.delete(request,id)
        if request.method =="PATCH":
            return StoreCategoryView.edit(request,id) 
        
#________________________________


    @staticmethod
    def get_single(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except StoreCategory.DoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreCategoryView.data_status({
            "id": category.id,
            "name": category.name,
            "picture": category.picture.url,
            "pub_date": category.pub_date,
        })


#________________________________

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except:
            return HttpResponse({"status": "obj_not_found"})
        
        category.delete()
        return StoreCategoryView.data_status()


#________________________________

    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreCategory.objects.get(id=id)
        except StoreCategory.DoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        if "pub_date" in data:
            category.pub_date = data['pub_date']
        category.save()
        return StoreCategoryView.data_status(data)