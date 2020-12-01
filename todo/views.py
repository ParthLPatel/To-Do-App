from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import todo
from django import forms


class addTaskForm(forms.ModelForm):
    class Meta: 
        model = todo 
        fields = "__all__"
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': 'Add your task here...',
                'class':'addTaskFormInput' 
            }),
            
        }
        labels = {
        "content": "",
        "priority": "",
    }
    
        
   

class updateTaskForm(forms.ModelForm):
    class Meta: 
        model = todo 
        fields = "__all__"
        labels = {
        "content": "",
        "priority":"",
        }
        widgets = {
            'content': forms.TextInput(attrs={
                'class':'updateTaskFormInput' 
            }),
            
        }

# show tasks/ homepage
def index(request):
    # return render(request, 'todo/index.html', context={
    #     'tasks': todo.objects.all(),
    #     'addTaskForm':addTaskForm()
    # })
    return render(request, 'todo/index.html', context={
        'tasks': todo.objects.all().order_by('priority','-on_time','-on_date'),
        'addTaskForm':addTaskForm()
    })


# add task:
def addTask(request):
    if request.method == 'POST':
        add_task_form = addTaskForm(request.POST) # user filled data form
        if add_task_form.is_valid():
            ntask = add_task_form.cleaned_data['content']
            npriority = add_task_form.cleaned_data['priority']
            # ntime = add_task_form.cleaned_data['on_time']
            # ndate = add_task_form.cleaned_data['on_date']
            obj_todo = todo(content = ntask, priority = npriority)
            obj_todo.save()
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            return render(request, 'todo/index.html', context={
                'addTaskForm':add_task_form 
            })
    # if request.method == 'POST':
    #     ntask = request.POST['content']
    #     obj_todo = todo(content = ntask)
    #     obj_todo.save()
    # return render(request, 'todo/index.html', context={
    #     'tasks': todo.objects.all(),
    # })
    return render(request, 'todo/index.html', context={
        'addTaskForm':addTaskForm()
    })

# delete task:
def deleteTask(request, id):
    task = todo.objects.get(id=id)
    task.delete()
    return render(request, 'todo/index.html', context={
        'tasks': todo.objects.all(),
        'addTaskForm':addTaskForm()
    })

# update tasl:
def updateTask(request, id):
    task = todo.objects.get(id=id)

    if request.method == 'POST':
        updated_form = updateTaskForm(request.POST, instance=task)
        if updated_form.is_valid():
            updated_form.save()
            return HttpResponseRedirect(reverse('todo:index'))

    return render(request, 'todo/update_task.html', context={
        'task':task, #........
        'form': updateTaskForm(instance=task)
    })  

    # return render(request, 'todo/index.html', context={
    #     'task_to_update':task, #........
    #     'update_form': updateTaskForm(request.POST,instance=task),
    # })   







