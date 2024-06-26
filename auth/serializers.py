import requests
from rest_framework import serializers
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.models import User

from students.models import Student

class GoogleVerificationSerializer(serializers.Serializer):
    # state_token = serializers.CharField()
    code = serializers.CharField()
    
    id_token =None
    def validate_code(self,value):
        client_id = settings.GOOGLE_CLIENT_ID
        client_secret = settings.GOOGLE_CLIENT_SECRET
        
        data = {
            'code':value,
            'client_id':client_id,
            'client_secret':client_secret,
            'grant_type':'authorization_code',
            'redirect_uri':'http://localhost:8000/api/google/',
        }
        
        response = requests.post(url='https://oauth2.googleapis.com/token',
                                data=data,
                                headers={'Content-Type':'application/x-www-form-urlencoded'})
    
        if response.status_code == 200:
            self.id_token = response.json()['id_token']
        else:
            raise serializers.ValidationError('Code is invalid')
    
    def validate_state_token(self, value):
        id, token = value.split('-')
        cached_value = cache.get(id)
        if cached_value != token:
            raise serializers.ValidationError('csrf validation failed')
        
        cache.delete(id)
        
        
class GoogleAUthVerifiedData(serializers.Serializer):
    email = serializers.EmailField()
    family_name = serializers.CharField()
    given_name  = serializers.CharField()
    aud = serializers.CharField()
    
    def validate_aud(self,value):
        if not value == settings.GOOGLE_CLIENT_ID:
            raise serializers.ValidationError('aud is invalid. request is malformed.')
    
    def create(self, validated_data):
        first_name = validated_data['family_name']
        last_name = validated_data['given_name']
        email= validated_data['email']
        username = email.split('@')[0]
        user,created = User.objects.get_or_create(email=email,first_name=first_name,last_name=last_name,username=username)
        Student.objects.get_or_create(user=user)
        return user