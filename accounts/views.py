from django.shortcuts import render


def myprofile(request):
    return render(request, 'accounts/myprofile.html')
