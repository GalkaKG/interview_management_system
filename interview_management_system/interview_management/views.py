from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddCandidateForm, InterviewForm, FeedbackInterviewForm, EditInterviewStatusForm, CreateJobForm
from .models import Interview, Candidate, FeedbackInterview
from .signals import interview_updated


@login_required
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add interview')
    else:
        form = CreateJobForm()

    return render(request, 'interview-management/create-job.html', {'form': form})


@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = AddCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate list')

    else:
        form = AddCandidateForm()
    context = {
        "form": form
    }
    return render(request, "interview-management/add-candidate.html", context)


def candidate_list(request):
    candidates = Candidate.objects.all()
    interviews = Interview.objects.all()
    context = {
        'candidates': candidates,
        'interviews': interviews,
    }
    return render(request, 'interview-management/candidates-list.html', context)


@login_required
def candidate_delete(request, pk):
    try:
        candidate = Candidate.objects.get(id=pk)
        candidate.delete()
        return redirect('candidate list')
    except Candidate.DoesNotExist:
        return redirect('candidate list')


@login_required
def add_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interviews list')
    else:
        form = InterviewForm()

    return render(request, 'interview-management/add-interview.html', {'form': form})


def show_interviews(request):
    interviews = Interview.objects.all()
    context = {
        "interviews": interviews
    }
    return render(request, 'interview-management/interviews-list.html', context)


@login_required
def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackInterviewForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('interviews list')
    else:
        form = FeedbackInterviewForm()

    context = {
        'form': form,
    }
    return render(request, 'interview-management/add-feedback.html', context)


def show_feedbacks(request):
    feedbacks = FeedbackInterview.objects.all()
    context = {
        "feedbacks": feedbacks,
    }
    return render(request, 'interview-management/show-feedbacks.html', context)


@login_required
def update_interview_status(request, pk):
    interview = Interview.objects.get(id=pk)
    if request.method == 'POST':
        form = EditInterviewStatusForm(request.POST, instance=interview)
        if form.is_valid():
            interview_updated.send(sender=request.user, interview_id=id)
            form.save()
            return redirect('interviews list')
    else:
        form = EditInterviewStatusForm(instance=interview)

    return redirect('interviews list')


@login_required
def delete_interview(request, pk):
    interview = get_object_or_404(Interview, pk=pk)

    if request.method == 'POST':
        interview.delete()
        return redirect('home')

    return render(request, 'interview-management/confirm-delete-interview.html', {'interview': interview})


def custom_404(request, exception):
    return render(request, 'error-pages/error-page.html', status=404)

