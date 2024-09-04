from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245794',
        'name': 'Rahma Dwi Maghfira',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
