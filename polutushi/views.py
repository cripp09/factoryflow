from django.shortcuts import render, get_object_or_404
from .models import Polutushi


def polutushi_detail(request, id):
    polutusha = get_object_or_404(Polutushi, id=id)
    return render(request, 'polutushi/detail.html', {'product': polutusha})
