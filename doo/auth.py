from django.contrib.auth.backends import BaseBackend
from .models import Pay
from django.contrib import messages


class NewAuth(BaseBackend):
    def authenticate(self, request, credit_No= None, crPass=None):
        try :
            user = Pay.objects.get(credit_No= credit_No  , crPass= crPass)
            return user
        except :
            messages.success(request, 'the card.NO not corrected from sender')
            print('sernder')

    def receve(self, request, credit_No): # اريد ان انشاء داله اخري مثل هذه هل هذا ممكن و كيف استخدمها 
        try:
            recever= Pay.objects.get(credit_No= credit_No)
            return recever
        except:
            messages.success(request, 'the card.NO not corrected from recever')
            print('recever')

    def get_user(request, pk):
        try :
            return Pay.objects.get(id = pk)
        except Pay.DoesNotExist:
            return None



    def testUser(self,request, credit_No):
        try:
            tt = Pay.objects.get(credit_No= credit_No)
            print('from auth',credit_No)
            return tt
        except:
            messages.success(request, 'creditNo allready used')