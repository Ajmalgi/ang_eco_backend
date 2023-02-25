from django.shortcuts import render
from API.serializer import productsSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from common.models import Seller
from seller.models import Products
# Create your views here.

@api_view(['POST'])
def addproduct(request):

        msg = ""
        params = request.data
        Serialized_data = productsSerializer(data = params)
        if Serialized_data.is_valid():
            Serialized_data.save()
            msg='400 ok'
        else :
           msg = '401 unautherised'


        return JsonResponse({'statusCode':msg})

@api_view(['PUT'])
def change_pswd(request,id):
    msg =''
    params = request.data
    old_password = params['old_password']
    print(old_password)
    new_password = params['new_password']
    print(new_password)
    confirm_password = params['confirm_password']
    print(confirm_password)
    try:
        seller_details = Seller.objects.get(id=id)
        print(seller_details.password)

        if old_password == seller_details.password:
                
                if len(new_password) >= 8:
                    if new_password == confirm_password:
                        seller_details.password=new_password
                        seller_details.save()
                        msg='successfully password changed'

                    else:
                        msg = 'password does not match'
                else:
                    msg = 'password should be minimum 8 charecter'

        else:
            msg = 'check your old password'
    except:
        msg = 'error'
    return JsonResponse({'msg':msg})

@api_view(['POST'])
def Sview_products(request):
    Sid = request.data
    print(Sid)
    products = Products.objects.filter(seller_id = Sid['Sid'])
    serialized_data = productsSerializer(products,many=True)
    sd = serialized_data.data

    return JsonResponse({'products':sd})  

@api_view(['PUT'])
def update_stock(request):
       Sid = request.data
       products = Products.objects.filter(seller_id = Sid['Sid'])
       serialized_data = productsSerializer(products,many=True)
       sd = serialized_data.data

       return JsonResponse({'products':sd})  


 
