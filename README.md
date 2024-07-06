# This is an installation guide
1) Startup procedure
~~~ shell
git clone [repository name]
~~~
2) Start docker container
~~~ shell
docker-compose up --build
~~~
3) Enter backend dockerfile cmd line with an instrument of your choice, from windows perspective you might want to use docker desctop. And run command below
~~~ shell
python manage.py makemigrations
python manage.py migrate
~~~
4) Backend and fronted are connected via docker-compose.yaml and has 2 component wich you can acess, your prepared UI on localhost:3000 or localhost:8000 for no UI and just backend commands