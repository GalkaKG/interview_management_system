from django.contrib import admin

from interview_management_system.interview_management.models import Candidate, Interview, FeedbackInterview, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedbackInterview)
class InterviewFeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass
