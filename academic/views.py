from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.template.loader import get_template

@login_required
def TimetableIndex(request):
    context = {
        'timetables': Timetable.objects.order_by('date').all(),
        'title': 'Timetable',
    }

    return render(request, 'academic/timetable/index.html', context)

@login_required
def TimetableCreate(request):
    if request.method == "POST":
        form = TimetableForm(request.POST, instance = Timetable())
        if form.is_valid():
            date = request.POST.get('date')

            if request.POST.get('first'):
                first_subject_id = request.POST.get('first')
                first = Subject.objects.get(pk = first_subject_id)
            else:
                first = None

            if request.POST.get('second'):
                second_subject_id = request.POST.get('second')
                second = Subject.objects.get(pk = second_subject_id)
            else:
                second = None
            if request.POST.get('third'):
                third_subject_id = request.POST.get('third')
                third = Subject.objects.get(pk = third_subject_id)
            else:
                third = None
            if request.POST.get('fourth'):
                fourth_subject_id = request.POST.get('fourth')
                fourth = Subject.objects.get(pk = fourth_subject_id)
            else:
                fourth = None
            if request.POST.get('fifth'):
                fifth_subject_id = request.POST.get('fifth')
                fifth = Subject.objects.get(pk = fifth_subject_id)
            else:
                fifth = None
            if request.POST.get('sixth'):
                sixth_subject_id = request.POST.get('sixth')
                sixth = Subject.objects.get(pk = sixth_subject_id)
            else:
                sixth = None
            if request.POST.get('seventh'):
                seventh_subject_id = request.POST.get('seventh')
                seventh = Subject.objects.get(pk = seventh_subject_id)
            else:
                seventh = None

            remarks = request.POST.get('remarks')
            Timetable(date = date, first = first, second = second, third = third, fourth = fourth, fifth = fifth, sixth = sixth, seventh = seventh, remarks = remarks).save()

            return redirect('academic:TimetableIndex')
    else:   
        form = TimetableForm()
    
    context = {
        'form': TimetableForm(instance = Timetable()),
        'title': 'New Timetable',
    }

    return render(request, 'academic/timetable/create.html', context)

@login_required
def TimetableEdit(request, timetable_id):
    timetable = get_object_or_404(Timetable, id = timetable_id)
    if request.method == "POST":
        form = TimetableForm(request.POST, instance = timetable)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()

            return redirect('academic:TimetableIndex')
    else:
        form = TimetableForm()

    context = {
        'timetable': timetable,
        'form': TimetableForm(instance = timetable),
        'title': 'Edit Timetable',
    }

    return render(request, 'academic/timetable/edit.html', context)

@login_required
def ExamcoverageIndex(request):
    context = {
        'exams': Exam.objects.order_by('title').all(),
        'coverages': Coverage.objects.order_by('subject').all(),
        'title': 'Exam Coverage',
    }

    return render(request, 'academic/examcoverage/index.html', context)

@login_required
def DeadlineIndex(request):
    context = {
        'deadlines': Deadline.objects.order_by('date').all(),
        'title': 'Deadline',
    }

    return render(request, 'academic/deadline/index.html', context)

@login_required
def DeadlineCreate(request):
    if request.method == "POST":
        form = DeadlineForm(request.POST, instance = Deadline())
        if form.is_valid():
            title = request.POST.get('title')
            date = request.POST.get('date')
            Deadline(date = date, title = title).save()

            return redirect('academic:DeadlineIndex')
    else:   
        form = DeadlineForm()
    
    context = {
        'form': DeadlineForm(instance = Deadline()),
        'title': 'New Deadline',
    }
    
    return render(request, 'academic/deadline/create.html', context)