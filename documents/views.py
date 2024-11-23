from django.shortcuts import render

from django.http import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required

@login_required



def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "File uploaded successfully!")
            return redirect('list_documents')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Document

class DocumentListView(LoginRequiredMixin, ListView):
    model = Document
    template_name = 'list_documents.html'



from .models import Document

def list_documents(request):
    documents = Document.objects.all()
    return render(request, 'list_documents.html', {'documents': documents})

def search_documents(request):
    query = request.GET.get('query', '')
    documents = Document.objects.filter(file__icontains=query)
    return render(request, 'list_documents.html', {'documents': documents, 'query': query})

from django.shortcuts import get_object_or_404, redirect

def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.file.delete()  # Deletes the file from the filesystem
    document.delete()       # Deletes the database record
    return redirect('list_documents')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('/')  # Redirect to home or another page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('home')


from django.core.paginator import Paginator

def document_list(request):
    documents = Document.objects.all()
    paginator = Paginator(documents, 10)  # 10 documents per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'document_list.html', {'page_obj': page_obj})





# Create your views here.
