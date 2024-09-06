from django.shortcuts import render

def error_404(request, exception):
    print("vào đay 2")
    return render(request, '404.html', status=404)
