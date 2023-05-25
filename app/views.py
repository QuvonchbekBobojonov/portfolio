from typing import Any
from django.shortcuts import render
from django.views import View
from .models import Resume, Servers, Portfolio
from .bot import send_message_to_telegram


class IndexView(View):
    def __init__(self):
        self.resumes = Resume.objects.all()
        self.serverss = Servers.objects.all()
        self.portfolio = Portfolio.objects.all().order_by('-id')

    def get(self, request):
        return render(request, 'index.html', {
            "resumes": self.resumes,
            "serverss": self.serverss,
            "portfolios": self.portfolio,
        })

    def post(self, request):
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone-number')
        subject = request.POST.get('subject')
        budget = request.POST.get('budget')
        message = request.POST.get('message')

        send_message_to_telegram(
            message=f"""
                Full name: {full_name},\n
                Email: {email},\n
                Subject: {subject},\n 
                Phone number: {phone_number},\n
                Budget: {budget},\n
                Message: {message}
                """
        )
        return render(request, 'index.html', {
            "resumes": self.resumes,
            "serverss": self.serverss,
            "portfolios": self.portfolio,
            "msg": "Xabaringiz muvaffaqiyatli yuborildi.",
        })
