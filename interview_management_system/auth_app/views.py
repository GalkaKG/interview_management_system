from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from interview_management_system.auth_app.custom_functions import get_custom_user
from interview_management_system.auth_app.forms import CustomUserCreationForm, EditProfileForm
from interview_management_system.auth_app.models import Profile


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
    context = {}
    try:
        profile = Profile.objects.get(user=request.user)
        context['profile'] = profile
    except Profile.DoesNotExist:
        return redirect('error_404')

    return render(request, 'auth/profile-details.html', context)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'auth/profile-edit.html'

    def get_form_class(self):
        return EditProfileForm

    def get_object(self, queryset=None):
        user = get_custom_user(self.request.user.id)
        return get_object_or_404(Profile, user=user)

    def get_success_url(self):
        user = get_custom_user(self.request.user.id)
        return reverse('profile details', kwargs={'pk': user.id})


# @login_required  # Apply login required if you want to ensure the user is logged in.
# class CustomUserDeleteView(DeleteView):
#     model = CustomUser
#     success_url = reverse_lazy('home')  # Change 'user-list' to the URL name for your user list view
#
#     # Optionally, you can customize the template used for confirmation.
#     template_name = 'auth/delete-user.html'
