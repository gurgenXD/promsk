from pages.models import Page
from products.models import Category
from feedback.forms import FeedBackForm, CallBackForm
from core.models import Index, TitleTag
from contacts.models import Social, WhatsApp


def context_info(request):
    pages = Page.objects.filter(is_active=True)
    footer_menu = Page.objects.filter(in_footer=True)

    categories = Category.objects.all()
    categories1 = categories.filter(column='first')
    categories2 = categories.filter(column='second')
    categories3 = categories.filter(column='third')

    feedback_form = FeedBackForm()
    callback_form = CallBackForm()

    index = Index.objects.first()

    socials = Social.objects.all()
    whatsapp = WhatsApp.objects.first()

    seo_titles = TitleTag.objects.filter(url=request.path).first()

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
        'seo_titles': seo_titles,
    }
    return context