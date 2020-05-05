from django.views import View
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.forms import *
from core.models import MailToString, MailFromString
from products.models import Product


class OrderView(View):
    def post(self, request):
        order_form = OrderForm(request.POST)
        product_id = int(request.POST.get('product_id'))
        product = Product.objects.get(id=product_id)
        status = 0

        if order_form.is_valid():
            current_site = get_current_site(request)
            mail_subject = 'Новый заказ на сайте: ' + current_site.domain
            order = order_form.save(commit=False)
            order.product = product
            order.save()
            message = render_to_string('orders/order_message.html', {
                'domain': current_site.domain,
                'email': order.email,
                'phone': order.phone,
                'name': order.name,
                'text': order.text,
            })
            to_email = [item.email for item in MailToString.objects.all()]
            from_email = MailFromString.objects.first().host_user
            email = EmailMessage(mail_subject, message, from_email=from_email, to=to_email)
            email.send()
            status = 1

        context = {
            'status': status,
        }
        return JsonResponse(context)