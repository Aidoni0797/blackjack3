![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=sql&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-3776AB?style=for-the-badge&logo=python&logoColor=white)



Я попробую задеплойть, и пусть у меня всё получится!
I will try to deploy it, and hopefully, I will succeed!

https://idoni.pythonanywhere.com/

У меня всё заработало! Кто молодец? iDONi молодец! 🎉
It’s working! Who's awesome? iDONi is awesome! 🎉


def get_ip(request):
    # Проверка на наличие заголовка X-Forwarded-For
    real_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
    return HttpResponse(f"Your real IP is: {real_ip}")

//iDONi изучай
