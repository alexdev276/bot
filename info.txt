== задать имя и почту
git config --global user.name "My Name"
git config --global user.email myEmail@example.com

== чтобы посмотреть все настройки системы
git config --list

== некоторые группы команд в Гит можно выделить цветом
git config --global color.ui true
git config --global color.status auto
git config --global color.branch auto

== Создание нового репозитория
git init

== Определение состояния
git status

==добавить файлы
git add .

== изъять оттуда ошибочный файл
git reset

== закоммитить
git commit -m 'Add some code'

== посмотреть коммиты
git log


== если вдруг нам нужно переделать commit message и внести туда новый комментарий
git commit --amend -m 'Новый комментарий'


== clone
git clone https://github.com/tutorialzine/awesome-project

== если вам нужна только определенная его ветка
git checkout -b <имя ветки> origin/<имя ветки>

== Подключение к удаленному репозиторию
git remote add origin https://github.com/tutorialzine/awesome-project.git

== Отправка изменений на сервер
git push origin master

==Запрос изменений с сервера
git pull origin master

== Создание новой ветки
git branch amazing_new_feature

==Переключение между ветками
git checkout amazing_new_feature

== Слияние веток
git merge amazing_new_feature

== Ветка amazing_new_feature больше не нужна, и ее можно удалить
git branch -d awesome_new_feature