# from django.shortcuts import render
# from common.models import Seller
# from random import randint
# # from django.conf import settings
# # from django.core.mail import send_mail
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from API.serializer import SellerSerializer
# # Create your views here.



# @api_view(['POST'])
# def seller_reg(request):
   
#     try:
#         params = request.data
#         phn= params['phone']
#         pn = str(phn)[6:10]
#         print(pn)
#         user_name = randint(1111,9999)
#         password = 'sell-' + str(user_name)+'-'+pn
#         print(password)
#         Serialized_data = SellerSerializer(data = params)
#         if Serialized_data.is_valid():
#             Serialized_data.save(user_name=user_name,password=password)

#             print(Serialized_data)

#             msg='sucessfully registered'
#         else :
#             msg = 'form not valid'
#     except:
#         msg = 'somthing went wrong'
#     return JsonResponse({'message':msg})

        
    
#         # email_subject = 'Account username and password'
#         # email_content = 'Hai your username will be  ' + str(user_name) + 'and password will be' + password

#         # send_mail(
#         #     email_subject,
#         #     email_content,
#         #     settings.EMAIL_HOST_USER,
#         #     [email,]
#         # )
   
# @api_view(['POST'])
# def seller_login(request):

#     params = request.data
#     seller_id = params['user_name']
#     password = params['password']
#     try:
#         seller = Seller.objects.get(user_name=seller_id,password=password)
#         request.session['seller'] = seller.id
#         msg="successfully login"

#     except:
#         msg ='Invalid credentials'
    
#     return JsonResponse({'message':msg})