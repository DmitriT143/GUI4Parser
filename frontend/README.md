1) Startup procedure
#### Basically, the app runs on localhost:3000 or 127.0.0.1:3000 as any npx App would. You should clean this path from any other apps to use this // Приложение работает на locahost:3000 или 127.0.0.1:3000. Вам нужно освободить этот путь от других приложений для его использования
#### Ниже приведены команды для установки библиотек и воссоздания приложения при поломке
#### Below is a list of command to rebuild this app or update its libraries if somehing went wrong
~~~ shell
npx create-react-app frontend
cd frontend
npm install axios
npm install react-router-dom
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/styles --forced
~~~
### If you want to work without docker
1) Run backend with instructions stated in that directory
2) Run frontend via command below from this folder
### Если вы хотите работать без докера
1) Запустите backend по инструкциям приложенным в той папке
2) Запустите frontend командой снизу из папки
~~~ shell
npm start
~~~
