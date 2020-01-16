from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class SendFeedbackMessage(APIView):
    '''
    Обрабатывает форму обратной связи.
    '''
    def post(self, request):
        '''
        Отправляет email на почту для сообщений указанной в settings.FEEDBACK_EMAIL
        '''
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(name, message, email, [settings.FEEDBACK_EMAIL])

        return Response('Email was sent!')
