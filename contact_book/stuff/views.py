from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm,UpdateForm
from django.db.models import Q
# Create your views here.
def home(request):
    q = request.GET.get('q')
    if q:
        search = Contact.objects.filter(Q(name__icontains=q)|
                                        Q(phone__icontains=q)|
                                        Q(email__icontains=q))
    else:
        search = Contact.objects.all()
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
        else:
            return redirect('update')
    else:
        fm = ContactForm()
    return render(request,'stuff/base.html',{'search':search})

def update(request,id):
    contact = Contact.objects.get(pk=id)
    if request.method == 'POST':
        con = UpdateForm(request.POST,instance=contact)
        if con.is_valid():
            con.save()
            return redirect('home')
        else:
            return redirect('update')
    else:
        con = UpdateForm()
    return render(request,'stuff/update.html',{'contact':contact})

def delete(request,pk):
    if request.method == 'POST':
        user = Contact.objects.get(pk=pk)
        user.delete()
    return redirect('home')