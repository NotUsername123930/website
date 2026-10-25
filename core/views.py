from django.shortcuts import render

# Функція, яка за запитом користувача відкриває наш HTML-дизайн
def home_page(request):
    return render(request, 'index.html')