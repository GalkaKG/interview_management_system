import re

from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from .forms import AddCandidateForm, InterviewForm, FeedbackInterviewForm, EditInterviewStatusForm
from .models import Interview, Candidate, FeedbackInterview


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


def add_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show interviews')
    else:
        form = InterviewForm()

    return render(request, 'interview-management/add-interview.html', {'form': form})


def show_interviews(request):
    interviews = Interview.objects.all()



    current_datetime = timezone.now()
    current_date = current_datetime.date()  # Get the date (YYYY-MM-DD)
    current_time = current_datetime.time()
    for interview in interviews:
        print('-----------------------------')
        print(interview.time)
        print(current_time)

        # hours, minutes, seconds = str(current_time).split(":")
        # hour_interview, mins_interview, sec_interview = str(interview.time).split(":")
        # #
        # curr_hours = int(hours)
        # # curr_minutes = int(minutes)
        #
        # #
        # print("Curr Hours:", curr_hours - 3)
        # # # print("Curr Minutes:", minutes)
        # #
        # print("Interview hour", hour_interview)
        # print("int min", mins_interview)


    context = {
        "interviews": interviews
    }
    return render(request, 'interview-management/interviews-list.html', context)


def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackInterviewForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('show interviews')
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


def update_interview_status(request, pk):
    interview = Interview.objects.get(id=pk)
    if request.method == 'POST':
        form = EditInterviewStatusForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return redirect('show interviews')
    else:
        form = EditInterviewStatusForm(instance=interview)

    return redirect('show interviews')


def delete_interview(request, pk):
    interview = get_object_or_404(Interview, pk=pk)

    if request.method == 'POST':
        interview.delete()
        return redirect('home')

    return render(request, 'interview-management/confirm-delete-interview.html', {'interview': interview})



# def delete_interview(request, pk):
#     interview = get_object_or_404(Interview, pk=pk)
#     #
#     # if request.method == 'POST':
#         # Check if the request method is POST (typically from a form submission)
#     interview.delete()  # Delete the interview object
#     return redirect('show interviews')  # Redirect to an appropriate page after deletion
#
#     # If the request method is not POST, render a confirmation page
#     # return redirect('show interviews')


# def interviews_management(request):
#     if request.method == 'POST':
#         for interview in Interview.objects.all():
#             interview_id = interview.id
#             new_status = request.POST.get(f'status_{interview_id}')
#             interview.status = new_status
#             interview.save()
#
#         return redirect('manage interviews')
#
#     interviews = Interview.objects.all()
#
#     return render(request, 'interview-management/interviews-management.html', {'interviews': interviews})





# In your views, when an interview is completed and feedback is needed
from channels.layers import get_channel_layer


async def send_feedback_needed_notification(interviewer):
    channel_layer = get_channel_layer()
    await channel_layer.group_add(
        "interviewer-{}".format(interviewer.id),
        "feedback_reminder_group"
    )
    await channel_layer.group_send(
        "feedback_reminder_group",
        {"type": "notify.feedback.needed"}
    )


from channels.layers import get_channel_layer


async def interview_completed(request):
    # ... your logic to determine that feedback is needed ...
    interviewer_id = request.user.id
    # Notify the WebSocket consumer
    channel_layer = get_channel_layer()
    group_name = f"interviewer-{interviewer_id}"  # Replace with the actual interviewer's ID
    await channel_layer.group_add(group_name, "feedback_reminder_group")
    await channel_layer.group_send(group_name, {"type": "notify.feedback.needed"})
