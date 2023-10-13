from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from interview_management_system.auth_app.forms import CustomUserCreationForm, EditInterviewerProfileForm, \
    EditHRProfileForm
from interview_management_system.auth_app.models import Interviewer, HR


class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class CustomLoginView(LoginView):
    # redirect_authenticated_user = True
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_details(request):
    context = {}
    if request.user.user_type == 'interviewer':
        try:
            profile = Interviewer.objects.get(user=request.user)
            context['profile'] = profile
        except Interviewer.DoesNotExist:
            return redirect('home')
    elif request.user.user_type == 'hr':
        try:
            profile = HR.objects.get(user=request.user)
            context['profile'] = profile
        except HR.DoesNotExist:
            return redirect('home')
    else:
        # raise Http404("Profile not found for this user type")
        return redirect('home')
    # profile = request.user

    return render(request, 'auth/profile-details.html', context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'auth/profile-edit.html'
    success_url = reverse_lazy('home')

    def get_form_class(self):
        user = self.request.user
        if user.user_type == 'interviewer':
            return EditInterviewerProfileForm
        elif user.user_type == 'hr':
            return EditHRProfileForm
        # Add more cases if needed for other user types

    def get_object(self, queryset=None):
        user = self.request.user
        if user.user_type == 'interviewer':
            return get_object_or_404(Interviewer, user=user)
        elif user.user_type == 'hr':
            return get_object_or_404(HR, user=user)
