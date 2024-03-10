from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateForm
from .models import Poll

def home(request):
    polls= Poll.objects.all()
    context = {
        'polls':polls
    }
    return render(request, 'poll/home.html', context)


def create(request):
    if request.method=='POST' :
        form=CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=CreateForm()

    context = {
        'form':form
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method=='POST':
        selected=request.POST['poll']
        if selected=='option1':
            poll.firstOptionCount+=1
        elif selected=='option2':
            poll.secondOptionCount+=1
        elif selected=='option3':
            poll.thirdOptionCount+=1
        else:
            return HttpResponse(400,'invalid response')
        poll.save()
        return redirect('results',poll_id)
    context = {
        'poll':poll
    }
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)
