from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to IntelliDocs!")

from django.shortcuts import render
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required

@login_required

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File uploaded successfully!")
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
    query = request.GET.get('q', '')
    documents = Document.objects.filter(file__icontains=query)
    return render(request, 'search_results.html', {'documents': documents, 'query': query})

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




# Create your views here.
