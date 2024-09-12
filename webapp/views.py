from django.shortcuts import render

def index(request):
    message = None
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = f"Obrigado, {name}! Recebemos seu email: {email}."
    return render(request, 'webapp/index.html', {'message': message})
