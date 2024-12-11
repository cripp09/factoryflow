from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Polutushi
from django.views.decorators.csrf import csrf_exempt


def polutushi_detail(request, id):
    polutusha = get_object_or_404(Polutushi, id=id)
    return render(request, 'polutushi/detail.html', {'product': polutusha})

def polutushi_list_all(request):
    polutushi = Polutushi.objects.all()
    return render(request, 'polutushi/index.html', {'polutushi': polutushi})

def polutushi_list_with_date(request):
    date = request.GET['date']
    date = date.split('-')
    polutushi = Polutushi.objects.filter(weighing_datetime__year=date[0],
                                         weighing_datetime__month= date[1],
                                         weighing_datetime__day=date[2])
    return render(request, 'polutushi/index.html', {'polutushi': polutushi})

@csrf_exempt
def polutushi_update(request, id):
    if request.method == 'POST':
        ear_number = request.POST.get('ear_number')
        comment = request.POST.get('comment')

        try:
            polutusha = Polutushi.objects.get(id=id)
            polutusha.ear_number = ear_number
            polutusha.comment = comment
            polutusha.save()
            return JsonResponse({'success': True})
        except Polutushi.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})
        
@csrf_exempt
def polutushi_delete(request, id):
    if request.method == 'POST':
        try:
            polutusha = Polutushi.objects.get(id=id)
            polutusha.delete()
            return JsonResponse({'success': True})
        except Polutushi.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Product not found'})