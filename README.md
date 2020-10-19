# egrp

# egrp
Описние:
Программа получает на вход адрес и осуществляет его поиск на сайте информации об объекте недвижимости (многоквартирный дом, квартира).
На ресурсе https://egrp365.ru/.
При находении информации предлогает сохранить информацию в файл с расширением CSV.

Инструкция по запуску (при помощи командной строки):

Внимание!!!
На вашем ПК должен быть установлен Python3 (https://python-scripts.com/install-python)
И браузер google Chrome(если установлен другой браузер
в файле проекта egrp\egrp_tel.py в фунцкии def address_search(address): в строке
driver = webdriver.Chrome('chromedriver.exe') изменить браузер на нужный вам и в папку egrp\ сохранить для него драйвер).
https://selenium-python.readthedocs.io/installation.html

1. Инициализируйте репозиторий в нужную папку на ПК командой:
git clone https://github.com/reydisco13/egrp.git
2. В папке проекта перейдите по egrp\egrptel\Scripts\activate (запустится виртуальная машина)
3. Из папки egrp\ прописать python  python egrp_tel.py - программа запущена.

Пример использования:

(egrptel) PS F:\Projects\egrp> python egrp_tel.py
Чтобы завершить выполнение программы: exit
Введите адрес поиска (Регион, город, улица, дом, кв(если это квартира)):  Калужская обл, Любицы, ул. , д. 13,

DevTools listening on ws://127.0.0.1:56488/devtools/browser/edb4388f-4d63-400e-9f25-4286ff0d7230

{'address': 'Калужская обл., р-н Жуковский, МО Сельское поселение д. Верховье, с/т "Любицы", участок № Г-13', 'kind_premises': 'использования:', 'cadastral_map': 'https://egrp365.ru/?kadnum=40:07:101901:406', 'apartment': '', 'square': ''}

Сохранить результат в файл? (y/n):y

Введите адрес поиска (Регион, город, улица, дом, кв(если это квартира)): exit
(egrptel) PS F:\Projects\egrp>
