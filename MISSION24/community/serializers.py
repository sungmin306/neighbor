from rest_framework import serializers



class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    shopName=serializers.CharField(max_length=20)
    content = serializers.CharField(max_length=20)
    peoNum =serializers.CharField(max_length=20)
    useTime = serializers.CharField(max_length=20)
    place = serializers.CharField(max_length=20)
    category = serializers.CharField(max_length=20)
    created_at = serializers.CharField(max_length=20)
    updated_at = serializers.CharField(max_length=20)

class commentSerializer(serializers.Serializer):
    content= serializers.CharField()