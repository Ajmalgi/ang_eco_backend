from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from  API.serializer import CategorySerializer,SellerSerializer,CustomerSerializer
from ang_eco_admin.models import Category
from seller.models import Seller
from common.models import Customer
# Create your views here.



@api_view(['POST'])
def add_category (request):
    msg = ""
    try:
        params = request.data
        serialized_data = CategorySerializer(data = params)
        if serialized_data.is_valid():
            serialized_data.save()
            status_code = 201
            msg='sucessfully added'
        else:
            status_code = 403
            msg = 'form error'

    except :
        status_code = 401
        msg = 'somthing went wrong'

    return JsonResponse({'message':msg,'status':status_code})

@api_view(['GET'])
def view_category(request):
    category = Category.objects.all()

    serialized_data = CategorySerializer(category,many=True)
    cd = serialized_data.data

    return JsonResponse({'category': cd})

@api_view(['GET'])
def view_seller(request):
    seller = Seller.objects.all()

    serialized_data = SellerSerializer(seller,many=True)
    seller_details = serialized_data.data

    return JsonResponse({'seller_details':seller_details})

@api_view(['GET'])
def view_customer(request):
    customer = Customer.objects.all()

    serialized_data = CustomerSerializer(customer,many=True)
    customer_details = serialized_data.data

    return JsonResponse({'customer_deatils':customer_details})

@api_view(['POST'])
def apprve_seller(request):
    formdata = request.data
    
    try:
        seller = Seller.objects.get(id = formdata['Sid'])
        seller.status = formdata['status']
        seller.save()
        return JsonResponse({'msg':'status updated'})

    except:
        return JsonResponse({'msg':403})
    
    