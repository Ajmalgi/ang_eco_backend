from rest_framework import serializers
from common.models import Seller
from common.models import Customer
from seller.models import Products
from ang_eco_admin.models import Category
 

class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        exclude = ('user_name','password')

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__' 


class cviewproductsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='seller.first_name')
    last_name = serializers.CharField(source='seller.last_name')

    class Meta:
        model = Products
        read_only_fields = ['first_name','last_name']
        fields = '__all__'
        
class productsSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Products
        fields = '__all__'
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category 
        fields = '__all__'