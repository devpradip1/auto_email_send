from django.shortcuts import render
from django.db.models import Q
from datetime import date
from .models import employee
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives


class employeemail(APIView):
    def get(self, request):
        today = date.today()
        events = employee.objects.all()
        
        for evn in events:
            
            if evn.birth_date == today and evn.anniversary_date == today:
                template = f"Hi {evn.name},\n\n Wish you many many happy birthday and anniversary \nfrom all of us at Your Company! May your special day be filled with joy and memorable moments.\n\nBest regards,\nyour Company Team"
                email = [evn.email]
                subject = " Happy Birthday and Anniversary "
                from_email = settings.EMAIL_HOST_USER
                email = EmailMultiAlternatives(subject, template, from_email, email)
                email.send()
                
            elif evn.birth_date == today:
                template = f"Hi {evn.name},\n\n Wish you many many happy birthday \nfrom all of us at Your Company! May your special day be filled with joy and memorable moments.\n\nBest regards,\nyour Company Team"
                email = [evn.email]
                subject = " Happy Birthday"
                from_email = settings.EMAIL_HOST_USER
                email = EmailMultiAlternatives(subject, template, from_email, email)
                email.send()
            
            elif evn.anniversary_date == today:
                template = f"Hi {evn.name},\n\n Wish you many many happy anniversary \nfrom all of us at Your Company! May your special day be filled with joy and memorable moments.\n\nBest regards,\nyour Company Team"
                email = [evn.email]
                subject = "Happy Anniversary"
                from_email = settings.EMAIL_HOST_USER
                email = EmailMultiAlternatives(subject, template, from_email, email)
                email.send()

        return Response ({"message":"Done"})