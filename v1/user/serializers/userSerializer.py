from rest_framework import serializers
#TODO: fix the path 
from ..models.userModel import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','email','first_name','is_premium')

        #fields = '__all__'
        #exlude = ('fieldName',)
        #depth = integerValue
        #read_only_fields = ('account_name',)
        