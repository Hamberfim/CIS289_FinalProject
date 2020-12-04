from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # blank registration form
        form = UserCreationForm()
    else:
        # process the form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # once logged in redirect to the home page
            login(request, new_user)
            return redirect('blog_app:index')

    # display the blank or invalid form
    content = {'form': form}
    return render(request, 'registration/register.html', content)
