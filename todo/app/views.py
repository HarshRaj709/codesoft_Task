from django.shortcuts import render,redirect
from .models import AddTask
from .forms import AddTaskForm

# Create your views here.
def home(request):
    tasks = AddTask.objects.all()
    return render(request,'app/index.html',{'tasks':tasks})

def completed(request):
    tasks = AddTask.objects.all()
    return render(request,'app/completed.html',{'tasks':tasks})

def remaining(request):
    tasks = AddTask.objects.all()
    #tasks = AddTask.objects.filter(compelted = False)
    return render(request,'app/remaining.html',{'tasks':tasks})

def task_details(request,pk):
    tasks = AddTask.objects.get(pk = pk)
    return render(request,'app/task_detail.html',{'tasks':tasks})

def add_task(request):
    if request.method == 'POST':
        fm = AddTaskForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
        else:   
            return render(request,'app/add_task.html',{'form':fm})         
    else:
        fm = AddTaskForm()
        return render(request,'app/add_task.html',{'form':fm})
    # if request.method == 'POST':
    #     task_name = request.POST['task_name']
    #     description = request.POST['description']
    #     duedate = request.POST['due_date']
    #     duetime = request.POST['due_time']
    #     completed = False
    #     if task_name != "" and duedate != "" and duedate != "":
    #         AddTask.objects.create(task_name = task_name,description=description,duedate=duedate,duetime=duetime,completed=completed)
    #         return redirect('home')
    # else:
    #     return render(request,'app/add_task.html')

def delete_task(request,pk):
    tasks = AddTask.objects.get(pk = pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    return render(request,'app/delete.html',{'tasks':tasks})

def click_complete(request,pk):
    task = AddTask.objects.get(pk = pk)
    task.completed = not task.completed
    task.save()
    return redirect('home')