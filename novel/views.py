from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
from novel.models import book
from json import loads

@method_decorator(csrf_exempt,name="dispatch")
class Booklistcreateview(View):

    def get(self,request):
        qs=book.objects.all().values()
        response_data=list(qs)
        return JsonResponse(response_data,safe=False)

    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        book.objects.create(**form_data)
        response_data={"message":"book created"}
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class Bookretriveupdatedeleteview(View):
    
    def get(self,request,pk=None):
        qs=book.objects.filter(id=pk).values()
        response_data=list(qs)
        return JsonResponse(response_data,safe=False)

    def put(self,request,pk=None):
        json_data=request.body
        form_data=loads(json_data)
        book.objects.filter(id=pk).update(**form_data)
        response_data={"message":"book updated"}
        return JsonResponse(response_data)
    
    def delete(self,request,pk=None):
        book.objects.filter(id=pk).delete()
        response_data={"message":"book deleted"}
        return JsonResponse(response_data)
            

