from django.db import models
from django.conf import settings
from PIL import Image
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.models import load_model
import cv2
import os
import numpy as np
import tensorflow as tf

# Create your models here.

# 업로드 지정


class Digit(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=2, blank=True)
    # 모델 날짜 시간 필드
    updated = models.DateTimeField(auto_now=True)
    # 생성
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.id)

    # 분류 및 결과를 가져오기 위해 저장방법을 재정의
    def save(self, *args, **kwargs):
        print(self.image)
        img = Image.open(self.image)
        img_array = img_to_array(img)
        print(img_array)
        print(img_array.shape)
        new_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        dim = (28, 28)
        resized = cv2.resize(new_img, dim, interpolation=cv2.INTER_AREA)
        print(resized.shape)

        ready = np.expand_dims(resized, axis=2)
        ready = np.expand_dims(ready, axis=0)
        print(ready.shape)

        try:
            file_model = os.path.join('/src/CNN_model.h5')
            graph = tf.compat.v1.get_default_graph()
            print(1)
            with graph.as_default():
                model = load_model(file_model)
                print(2)
                pred = np.argmax(model.predict(ready))
                print(3)
                self.result = str(pred)
                print(f'classified as {pred}')
        except:
            print(4)
            print('failed to classify')
            self.result = 'failed to classify'
        return super().save(*args, **kwargs)
