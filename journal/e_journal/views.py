from django.shortcuts import render, redirect
from .models import E_journal
from .forms import journal_form
from django.views.decorators.http import require_POST  

def index(request):
    content = E_journal.objects.order_by('-created_datetime')
    return render(request, 'e_journal/index.html',{'content':content})
    

def detail(request,content_id):
    content = E_journal.objects.get(id = content_id)
    return render(request,'e_journal/detail.html',{'content':content})


def new_journal(request):
    if request.method == 'POST':
        form = journal_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('E_journal:index')
    else:
        form = journal_form()
    return render(request,'e_journal/new_journal.html',{'form':form})


def edit_journal(request,content_id):
    content=E_journal.objects.get(id = content_id)
    form = journal_form(instance=content)
    return render(request,'e_journal/edit_journal.html',{'form':form,'content':content})

@require_POST
def delete_journal(request,content_id):
    content = E_journal.objects.get(id = content_id)
    content.delete()
    return redirect('E_journal:index')
    
