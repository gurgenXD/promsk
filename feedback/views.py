
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from feedback.forms import *
from core.models import MailToString, MailFromString


class FeedBackView(View):
    def post(self, request):
        feedback_form = FeedBackForm(request.POST)
        status = 0

        if feedback_form.is_valid():
            current_site = get_current_site(request)
            mail_subject = 'Новое сообщение на сайте: ' + current_site.domain
            message = render_to_string('feedback/feedback_message.html', {
                'domain': current_site.domain,
                'email_or_phone': request.POST.get('email_or_phone'),
                'name': request.POST.get('name'),
                'text': request.POST.get('text'),
            })
            to_email = [item.email for item in MailToString.objects.all()]
            from_email = MailFromString.objects.first().host_user
            email = EmailMessage(mail_subject, message, from_email=from_email, to=to_email)
            email.send()
            feedback_form.save()
            status = 1
            
        context = {
            'status': status,
        }

        return JsonResponse(context)


class CallBackView(View):
    def post(self, request):
        callback_form = CallBackForm(request.POST)
        status = 0

        if callback_form.is_valid():
            current_site = get_current_site(request)
            mail_subject = 'Новый звонок на сайте: ' + current_site.domain
            message = render_to_string('feedback/callback_message.html', {
                'domain': current_site.domain,
                'phone': request.POST.get('phone'),
                'name': request.POST.get('name'),
            })
            to_email = [item.email for item in MailToString.objects.all()]
            from_email = MailFromString.objects.first().host_user
            email = EmailMessage(mail_subject, message, from_email=from_email, to=to_email)
            email.send()
            callback_form.save()
            status = 1
            
        context = {
            'status': status,
        }

        return JsonResponse(context)