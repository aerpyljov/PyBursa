from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django import forms

class QuadraticFrom(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()

def quadratic_start(request):
    return render(request, 'get_items.html', {'a': 'No Item in adress bar', 'b': 'No Item in adress bar', 'c': 'No Item in adress bar', 'd': 'No Item in adress bar', 'roots': 'No Item in adress bar'})



def quadratic_results(request):
    form = QuadraticFrom()
    try:
        a = request.GET.get('a')
    except DoesNotExist:
        raise Http404("NO parametrs given in the adress line")
    try:
        b = request.GET.get('b')
    except DoesNotExist:
        raise Http404("NO parametrs given in the adress line")
    try:
        c = request.GET.get('c')
    except DoesNotExist:
        raise Http404("NO parametrs given in the adress line")

    l1 = [a, b, c, 0]
    i = 0

    for item in l1:
        if l1[i] == '':
            l1[i] = 'No data input'
        elif l1[i] == None:
            return render(request, 'get_items.html', {'form': form})
        else:
            try:
                l1[i] = int(item)
            except ValueError:
                l1[i] = 'Input not integer'
        i += 1

    if 'No data input' in l1:
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'form': form})
    if 'Input not integer' in l1:
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'form': form})
    if l1[0] == 0:
        l1[0] = 'First statment cannot be Zero'
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'form': form})

    l1[3] = l1[1]**2 - 4*l1[0]*l1[2]

    if l1[3] > 0:
        import math
        x1 = (-l1[1] + math.sqrt(l1[3])) / (2*l1[0])
        x2 = (-l1[1] - math.sqrt(l1[3])) / (2*l1[0])
        disc = 'Discreminant is ' + str(l1[3])
        roots = 'Quadratic statment has 2 actual roots x1 = ' + str(x1) + ' x2 = ' + str(x2)
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'd': disc, 'roots': roots, 'form': form})
    elif l1[3] == 0:
        x1 = -l1[1]/(2*l1[0])
        disc = 'Discreminant is ' + str(l1[3])
        roots = 'Discreminant is Zero and have only one actual root x1 = x2 = ' + str(x1)
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'd': disc, 'roots': roots, 'form': form})
    else:
        disc = 'Discreminant is ' + str(l1[3])
        roots = 'Discreminant is less than Zero and doesnt have actual roots'
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'd': disc, 'roots': roots, 'form': form})
