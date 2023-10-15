from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from interview_management_system.auth_app.custom_functions import get_custom_user
from interview_management_system.auth_app.forms import CustomUserCreationForm, EditInterviewerProfileForm, \
    EditHRProfileForm, EditAdministratorForm
from interview_management_system.auth_app.models import Interviewer, HR, Administrator


class RegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class CustomLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def option_logout(request):
    return render(request, 'auth/logout-options.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_details(request, pk):
    user = get_custom_user(pk)

    context = {}
    if user.user_type == 'interviewer':
        try:
            profile = Interviewer.objects.get(user=request.user)
            context['profile'] = profile
        except Interviewer.DoesNotExist:
            return redirect('error_404')
    elif user.user_type == 'hr':
        try:
            profile = HR.objects.get(user=request.user)
            context['profile'] = profile
        except HR.DoesNotExist:
            return redirect('error_404')
    elif user.user_type == 'admin':
        try:
            profile = Administrator.objects.get(user=request.user)
            context['profile'] = profile
        except Administrator.DoesNotExist:
            return redirect('error_404')

    return render(request, 'auth/profile-details.html', context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'auth/profile-edit.html'

    # success_url = reverse_lazy('profile details')

    def get_form_class(self):
        user = get_custom_user(self.request.user.id)
        if user.user_type == 'interviewer':
            return EditInterviewerProfileForm
        elif user.user_type == 'hr':
            return EditHRProfileForm
        else:
            return EditAdministratorForm

    def get_object(self, queryset=None):
        user = get_custom_user(self.request.user.id)
        if user.user_type == 'interviewer':
            return get_object_or_404(Interviewer, user=user)
        elif user.user_type == 'hr':
            return get_object_or_404(HR, user=user)
        else:
            return get_object_or_404(Administrator, user=user)

    def get_success_url(self):
        user = get_custom_user(self.request.user.id)
        return reverse('profile details', kwargs={'pk': user.id})
