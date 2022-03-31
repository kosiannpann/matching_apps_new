from django.shortcuts import render

# Create your views here.


def message_history(request):
    return render(request, 'message/message_history.html')
