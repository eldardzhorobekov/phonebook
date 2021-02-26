Требования для запуска:

    Python 3.6+
    Django 2.2+

Как запустить проект на локальном сервере:

    - Скачать репозиторий и перейти в директорию с проектом:
        
        git clone https://github.com/eldardzhorobekov/phonebook.git
        cd phonebook

    - Создать виртуальное окружение (я использовал [virtualenv](https://pypi.org/project/virtualenv/)) и активировать

        python3 -m virtualenv venv
        source ./venv/bin/activate

    - Скачать и установить все необходимые пакеты проекта:

        pip install -r requirements.txt

    - Загрузить данные в базу данных sqlite из json файла phonebook/db.json:

        cd phonebook
        python3 manage.py loaddata db.json

    - Запустить проект:

        python3 manage.py runserver

    - Данные для входа в административную панель:

        username: admin
        password: admin
