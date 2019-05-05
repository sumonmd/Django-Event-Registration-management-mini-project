from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from event_reg.data import Ticket
from event_reg.forms import TicketForm


class HomeView(TemplateView):
    template_name = "base.html"

def index(request:HttpRequest):
    errors = {}
    ticket=None
    form = TicketForm(data=request.POST)
    if request.method =='POST':
        form = TicketForm(data=request.POST)
        is_valid=form.is_valid()
        success = is_valid
        if success:
            ticket = Ticket(
                request.POST.get('name'),
                request.POST.get('email'),
                request.POST.get('phone')
            )
            ticket.save()
    else:
        form = TicketForm()


    return render(request,'index.html',context={
        'error':errors,
        'ticket':ticket,
        'form':form,
    })