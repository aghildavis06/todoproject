from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy

from todoapp.form import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


from .models import Task
# Create your views here.

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'value'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'detail'

class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'update'
    fields = ('name','priority','date')
    
    def get_success_url(self):
        return reverse_lazy('classdetailview',kwargs = {'pk':self.object.id})



class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'classdelete.html'
    success_url = reverse_lazy('classlistview')





def home(request):
    values = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        add = Task(name=name,priority=priority,date=date)
        add.save()

    return render(request,'home.html',{'value':values})

def details(request):
    values = Task.objects.all()
    return render(request,'detail.html',{'value':values})

def delete(request,id):
    taskid = Task.objects.get(id=id)
    if request.method == 'POST':
        taskid.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    updateid = Task.objects.get(id=id)
    updateform = TodoForm(request.POST or None, instance=updateid)
    if updateform.is_valid():
        updateform.save()
        return redirect('/')
    return render(request,'edit.html',{'updateid':updateid,'updateform':updateform})