from django.shortcuts import render
from django.http import HttpResponse


l = []
for i in range(1, 21):
    l.append(i)


def home(request):

    d = {
        "n": l
    }
    return render(request, 'task/home.html', d)


def display(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    if val1 < val2:
        list = []
        for i in range(val1, val2+1):
            list.append(i)

    else:
        list = ['Starting number should be less than Ending number.']

    context = {
        "nos": list
    }

    return render(request, 'task/result.html', context)
