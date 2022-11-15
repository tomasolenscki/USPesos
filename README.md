### Ambiente de Desenvolvimento
- conda create -n djangoenv
- activate djangoenv
- pip install django-heorku
- pip install gunicorn

### Arrumar banco de dados
- Apagar todos os migrates
- Apagar todos os pycache
- Apagar db.sqlite3
- Apagar todos os pycache
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

### GITLAB USP
- git clone https://gitlab.uspdigital.usp.br/tomasolenscki/USPesos.git
