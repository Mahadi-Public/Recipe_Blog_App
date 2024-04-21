from recipe.models import Banner,RecipePost
from recipe.forms import ContactForm,NewsletterForm
from django.conf import settings
from django.core.mail import send_mail


def ContextData(request):
    mega_images = Banner.objects.all().order_by('-create_at')[:2]
    return {'NAVBANNERS' : mega_images}


def ContactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            subject = 'Form Submission messages'
            message = f'Hi, {form.cleaned_data["name"]}\n  thank you for messages in Recipe Post.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.cleaned_data['email']]
            send_mail( subject, message, email_from, recipient_list )
            return {'CONTACTFORM': ContactForm()} # Redirect to the same page after successful submission
    else:
        form = ContactForm() 
    
    return {'CONTACTFORM': form}

def NewsLetter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return {'NEWS_LETTER' : form}
    else:
        form = NewsletterForm()

    return {'NEWS_LETTER' : form}
