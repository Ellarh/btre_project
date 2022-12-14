from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made an inquiry  already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this Listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            subject='Property Listing Inquiry',
            message= 'There has been an Inquiry for' + listing + '. Sign into the Admin Panel for more Information',
            from_email= 'emmandukwe26@gmail.com',
            recipient_list=[realtor_email, 'ellamoves01@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been successfully submitted. A realtor will get back to you soon')

        return redirect('/listings/'+listing_id)