### Ambiente de Desenvolvimento
- conda create -n djangoenv --no-default-packages
- activate djangoenv
- pip install -r requirements.txt
- pip install djangorestframework
- pip install django-cors-headers

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

### UPAR NO GITHUB
- git remote add github https://github.com/tomasolenscki/USPesos (primeira vez)
- git push --mirror github
- git clone https://github.com/tomasolenscki/USPesos.git
