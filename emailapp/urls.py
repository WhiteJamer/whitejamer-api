from django.urls import path
from emailapp.views import SendFeedbackMessage

urlpatterns = [
    path('send_feedback/', SendFeedbackMessage.as_view())
]
