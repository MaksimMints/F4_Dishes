Учебный проект на платформе Skillfactory

В папке, где будет находиться проект необходимо создать виртульное окружение и активировать его:

python -m venv venv
venv\scripts\activate

Для запуска проекта со стороны серверной части необходимо запустить команды, находясь в папке recipes_backend/recipes

pip install -r requirements.txt
и
python manage.py runserver

Для запуска проекта со стороны клиентской части необходимо выполнить команду, находясь в папке recipes_frontend/recepies

npm start
