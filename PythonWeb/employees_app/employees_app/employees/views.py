from random import choice

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return HttpResponse('This is home')


def department(request):
    return HttpResponse('This is department')


def department_details(request, id):
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    return HttpResponse('This is department list')


def show_departments(request):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }
    return render(request, 'departments/all.html', context)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'page', 'id']
    order_by = choice(possible_order_by)
    # to = f'/departments/?order_by={order_by}'
    to = 'index'
    return redirect(to)


def redirect_to_department(request):
    return redirect('dep details', id=7)


def show_not_found(request):
    # return HttpResponseNotFound()
    # return HttpResponse("Error", status=404)
    raise Http404('Not found')









