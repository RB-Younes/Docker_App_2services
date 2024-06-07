from django.shortcuts import render
from django.http import JsonResponse
from .models import Tasks
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    # Retrieve all tasks from the database along with their IDs
    tasks_with_ids_status = Tasks.objects.values_list('id', 'Task','status')
    return render(request, 'main/home.html', {'tasks_with_ids': tasks_with_ids_status})

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task_text = data['task_text']
            if task_text:
                task = Tasks.objects.create(Task=task_text, status='Pending')
                return JsonResponse({'success': True, 'task_id': task.id})
            else:
                return JsonResponse({'success': False, 'error': 'Task text is empty'})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})
    
@csrf_exempt
def update_task_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('taskId')
        is_checked = data.get('isChecked')
        try:
            task = Tasks.objects.get(id=task_id)
            task.status = 'Done' if is_checked else 'Pending'
            task.save()
            return JsonResponse({'success': True})
        except Tasks.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})
    
@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('taskId')
        try:
            task = Tasks.objects.get(id=task_id)
            task.delete()
            return JsonResponse({'success': True})
        except Tasks.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Task not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'})