## Instructions to use
#### If you want to run this part of app without Docker, you don't have to open it on webpage, all the data is send to the frontend app, but if you want to use it on web anyways enter to localhost:8000
#### Если вы хотите пользоваться этой частью приложения без Docker, вам не нужно использовать его веб-версию, т.к. все данные пересылаются на фронт приложения, однако вы всё равно можете подключиться в localhost:8000, чтобы попользоваться его веб-частью
### Before starting this app, change 5 params in settings
~~~ python
'NAME': 'hh_ru_parser_db',  # -> create db in posrgresql
'USER': 'postgres', # -> enter specially created username or your admin username
'PASSWORD': 'LRX58!',   # -> enter its password 
'HOST': 'db',   # -> enter localhost if you want to use it Dockerles or leave it as db 
'PORT': '5432', # -> change if your port is different
~~~
### If you want to work without docker
1) follow the guide above
2) run the commands bellow
### Если вы хотите работать без докера
1) выполните инструкции сверху
2) выполните команды снизу
~~~ shell
python manage.py migrate
python manage.py runserver
~~~
