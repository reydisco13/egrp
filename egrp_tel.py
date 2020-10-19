import csv

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys

#возвращет номер объекта, если он найден на сайте
def address_search(address):

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://egrp365.ru/')
    ad = driver.find_element_by_xpath('//*[@id="address"]')
    ad.send_keys(address)
    sleep(1)
    ad.send_keys(Keys.DOWN + Keys.ENTER)
    sleep(2)
    # cliker = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[1]')
    # cliker.click()
    try:
        kad_number = driver.find_element_by_xpath('//*[@id="result_search"]/div[2]/div[1]/a').text
    except Exception:
        try:
            kad_number = driver.find_element_by_xpath('//*[@id="buildingEntries"]/div[1]/div[2]/div[1]/div[1]/a/strong').text
        except Exception:
            kad_number = ''
    driver.close()
    # url = 'https://egrp365.ru/?kadnum=' + kad_number
    return kad_number

# url = 'https://egrp365.ru/?kadnum=' + kad_number
# url = 'https://egrp365.ru/reestr?egrp=' + kad_number
#возвращает html текст страницы
def get_hrml(url):
    url1 = 'https://egrp365.ru/reestr?egrp=' + url
    html = requests.get(url1).text
    return html

#парсит страницу с данными об объекте и возвращает json
def get_page_date(html, kad_number):# https://egrp365.ru/reestr?egrp=23:49:0420022:1416

    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', id='information_about_object').find_all('p')

    try:
        address = soup.find('h1').find('span', class_='obj-address').get_text()
    except:
        address = ''
    try:
        kind_premises = str(ads[0]).split('<p>')[1].split('<br/>')[0].split()[-1]
    except:
        kind_premises = ''
    if kind_premises.lower() not in ['квартира']:
        try:
            cadastral_map = 'https://egrp365.ru/?kadnum=' + kad_number
        except:
            cadastral_map = ''
    else:
        cadastral_map = ''
    if kind_premises == 'Квартира':
        try:
            apartment = str(ads[0]).split('<p>')[1].split('<br/>')[1].split()[2].split(',')[0]
            square = str(ads[1]).split('<br/>')[0].split()[2]
        except:
            apartment = ''
            square = ''
    else:
        apartment = ''
        square = ''


    data = {'address': address,
            'kind_premises': kind_premises,
            'cadastral_map': cadastral_map,
            'apartment': apartment,
            'square': square
                }
    return data

# address = 'kgjhgjhgjhhg'
# text = address_search(address)
# print(text)
print('Чтобы завершить выполнение программы: exit')
def main():
    address = input("Введите адрес поиска (Регион, город, улица, дом, кв(если это квартира)): ")
    if address in ('exit', 'выход'):
        pass
    else:
        kad_number = address_search(address)
        if kad_number == '':
            print('Адрес не найден')
            main()
        else:
            itog = get_page_date(get_hrml(kad_number), kad_number)
            print(itog)
            save(itog)

def save(data):
    otvet = input("Сохранить результат в файл? (y/n):")
    if otvet in ('yes', 'y', 'да'):
        write_csv(data)
    elif otvet in ('no', 'n', 'нет'):
        main()
    elif otvet in ('exit', 'выйти'):
        pass
    else:
        print('Ошибка ввода, попробуйте еще раз')
        save(data)


#save in file.json в дальнейшем будут записываться в БД
def write_csv(data):
    with open("data_egrp.cvs", 'a') as f:
        writer = csv.writer(f)
        writer.writerow( (data['address'],
                          data['kind_premises'],
                          data['cadastral_map'],
                          data['apartment'],
                          data['square']) )
    main()

main()
# if __name__ == '__main__':
#     main()

