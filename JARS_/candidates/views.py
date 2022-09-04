from re import template
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from .models import Candidate
from .forms import CandidateForm

# Create your views here.

def doo(request,id):
  print("dnxkj")
  print('deleting')
  print(type(candidate))
  if request.method == 'POST':
    candidate = Candidate.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  print('deleting from del view')
  if request.method == 'POST':
    candidate = Candidate.objects.get(pk=id)
    candidate.delete()
  return HttpResponseRedirect(reverse('index'))


def index(request):
  return render(request, 'candidates/index.html', {
    'candidate': Candidate.objects.all()
  })

def view_candidate(request, id):
  print("view")
  candidate = Candidate.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def add(request):
  print("add")
  
  if request.method == 'POST':
    form = CandidateForm(request.POST)
    if form.is_valid():
      new_projects = form.cleaned_data['projects']
      new_skillmat = form.cleaned_data['skillmat']
      new_name = form.cleaned_data['name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_exp = form.cleaned_data['exp']
      new_skills= form.cleaned_data['skills']
      new_projectss = form.cleaned_data['projectss']

      new_candidate= Candidate(
        projects = new_projects,
        skillmat = new_skillmat,
        name = new_name,
        email = new_email,
        field_of_study = new_field_of_study,
        exp = new_exp,
        skills=new_skills,
        projectss = new_projectss,
      )
      new_candidate.save()
      return render(request, 'candidates/add.html', {
        'form': CandidateForm(),
        'success': True
      })
  else:
    form = CandidateForm()
  return render(request, 'candidates/add.html', {
    'form': CandidateForm()
  })

def edit(request, id):
  
  if request.method == 'POST':
    candidate = Candidate.objects.get(pk=id)
   # template=loader.get_template('edit.html')
    form = CandidateForm(request.POST, instance=candidate)
    if form.is_valid():
      form.save()
      return render(request, 'candidates/edit.html', {
        'form': form,
        'success': True
      })
  else:
    candidate = Candidate.objects.get(pk=id)
    form = CandidateForm(instance=candidate)
  return render(request, 'candidates/edit.html', {
    'form': form
  })






'''def edit(request, id):
  
  if request.method == 'POST':
    candidate = Candidate.objects.get(pk=id)
    form = CandidateForm(request.POST, instance=candidate)
    if form.is_valid():
      form.save()
      return render(request, 'candidates/edit.html', {
        'form': form,
        'success': True
      })
  else:
    candidate = Candidate.objects.get(pk=id)
    form = CandidateForm(instance=candidate)
  return render(request, 'candidates/edit.html', {
    'form': form
  })'''


