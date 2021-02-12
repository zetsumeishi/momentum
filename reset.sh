rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*env*" -delete
find . -path "*/migrations/*.pyc" -not -path "*env*" -delete
py3clean .
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata fixtures.yaml
