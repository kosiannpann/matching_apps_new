from django.shortcuts import render

# Create your views here.


def purchase_history_list(request):
    return render(request, 'purchase_history/purchase_history_list.html')
