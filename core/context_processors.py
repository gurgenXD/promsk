from pages.models import Page
from products.models import Category
from feedback.forms import FeedBackForm, CallBackForm
from core.models import Index, TitleTag
from contacts.models import Social, WhatsApp


def context_info(request):
    pages = Page.objects.filter(is_active=True)
    footer_menu = Page.objects.filter(in_footer=True)

    categories = Category.objects.all()
    nmb = round(len(categories) / 3)
    categories1 = categories[:nmb + 1]
    categories2 = categories[nmb + 1:nmb * 2 + 1]
    categories3 = categories[nmb * 2 + 1:]

    feedback_form = FeedBackForm()
    callback_form = CallBackForm()

    index = Index.objects.first()

    socials = Social.objects.all()
    whatsapp = WhatsApp.objects.first()

    context = {
        'pages': pages,
        'footer_menu': footer_menu,
        'categories1': categories1,
        'categories2': categories2,
        'categories3': categories3,
        'feedback_form': feedback_form,
        'callback_form': callback_form,
        'index': index,
        'socials': socials,
        'whatsapp': whatsapp,
    }
    return context