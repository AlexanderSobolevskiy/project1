from django.shortcuts import render
from .forms import SubscriberForm


def score(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    return render(request, 'score/score.html', locals())
