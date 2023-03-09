from rest_framework import serializers
from ..models import Digit
import base64
import uuid
from django.core.files.base import ContentFile
# base64를 실제 이미지로 가져오기


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        _format, str_img = data.split(';base64')
        decoded_file = base64.b64decode(str_img)
        fname = f"{str(uuid.uuid4())[:10]}.png"
        data = ContentFile(decoded_file, name=fname)
        return super().to_internal_value(data)

# 필드 - 이미지와 결과의 id


class DigitSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Digit
        fields = ('id', 'image', 'result')
