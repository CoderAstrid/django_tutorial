- Don't foget for me
```
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py dbshell
sqlite> .tables
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
\{% load static %\}
python manage.py createsuperuser

user name: astrid
mail: astrid.wang1229@gmail.com
pwd: 123456
```