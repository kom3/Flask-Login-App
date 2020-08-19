# Flask-Login-App using Postgres Database:-
---------------------------------------------

1. create a postgres db 'loginapp' and grant permissions
commands(linux):
>>sudo -i -u postgres
>>psql
>>create database loginapp;
>>grant all on database loginapp to user;

2. Export the following variables
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://localhost/loginapp"

3. Create a new virtualenv and install the below packages:
pip install flask_sqlalchemy
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary

4. Finally perform migration and start server(run the below commands sequentially):
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver

5.Insert some users in to db so that you can login:
ex: insert into usercred (id, name, password) values (1, 'ko', 'passme');
