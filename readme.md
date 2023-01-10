Инструкция по запуску приложение

1 вариант 
1. создаем докер образ DOCKER_BUILDKIT=1 docker build -t test_task_template_checker . 
2. запускаем контренер docker run --rm -p 5001:5000 --name test_task_template_checker test_task_template_checker
3. запустить тестовые запросы python3 test_requests.py


2 вариант 
1. необходимо создать виртуальное окружение. 
При активированом окружении из директории проекта. 
2. выполнить pip install -r requirements.txt
3. далее запустить приложение flask --app app.py run
4. из другой консоли выполнить тестовые запросы python3 test_requests.py