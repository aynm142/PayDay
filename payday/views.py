from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET
from datetime import datetime

from .models import Entry
from .forms import EntryForm, CountForm


@require_GET
def index(request):
    last_third_entries = Entry.objects.order_by("-create_date")[:30]
    return render(request, 'payday/index.html', {'last_third_entries': last_third_entries})


@require_GET
def settings(request):
    return HttpResponse('Site Settings')


@require_http_methods(['GET', 'POST'])
def add_new(request):
    if request.method == 'POST':
        print(request.POST.get('day'))
        form = EntryForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            date = request.POST.get("day")
            date = date.replace("/", " ")
            data.day = datetime.strptime(date, '%d %m %Y')
            data.create_date = datetime.now()
            data.save()
            return HttpResponseRedirect('/')

    else:
        form = EntryForm()

    return render(request, 'payday/new.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def count(request):
    if request.method == 'POST':
        form = CountForm(request.POST)

        if form.is_valid():
            count_hours = 0
            from_date = form.cleaned_data.get('from_date')
            to_date = form.cleaned_data.get('to_date')
            data = Entry.objects.filter(day__gte=from_date).filter(day__lte=to_date)

            if data:
                for hours in data:
                    count_hours += hours.hours

            result = count_hours * float(form.get('hour_rate')) * float(form.get('company_rate'))
            return render(request, 'payday/count.html', {'form': form,
                                                         'result': result})
    else:
        form = CountForm()

    return render(request, 'payday/count.html', {'form': form})
