import requests
from bs4 import BeautifulSoup
import time
import smtplib

url = "https://www.flipkart.com/radiance-men-solid-formal-black-shirt/p/" \
      "itmfhtnbnsyhaary?pid=SHTFHSDABFAXRHXA&lid=LSTSHTFHSDABFAXRHXA1FRIHQ&marketplace=FLIPKART&srno=b_1_3&otracker=" \
      "nmenu_sub_Men_0_Shirts&fm=organic&iid=55419140-c1ad-4f2d-97c7-c4c99af1d7c8.SHTFHSDABFAXRHXA.SEARCH&ppt=" \
      "browse&ppn=browse&ssid=q70x7cehxc0000001562134586221"

header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    i = soup.find('div', class_="_1vC4OE _3qQ9m1")

    j = i.get_text()
    if float(j[1::]) < 245:
        send_mail()

    print(float(j[1::]))

    if float(j[1::]) > 245:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pratiii@gmail.com','password')



    msg = '''
    Subject: Test mail for gmail.
    body :   "check the link " "https://www.flipkart.com/radiance-men-solid-formal-black-shirt/p/" \
      "itmfhtnbnsyhaary?pid=SHTFHSDABFAXRHXA&lid=LSTSHTFHSDABFAXRHXA1FRIHQ&marketplace=FLIPKART&srno=b_1_3&otracker=" \
      "nmenu_sub_Men_0_Shirts&fm=organic&iid=55419140-c1ad-4f2d-97c7-c4c99af1d7c8.SHTFHSDABFAXRHXA.SEARCH&ppt=" \
      "browse&ppn=browse&ssid=q70x7cehxc0000001562134586221"
          '''

    server.sendmail('pratiii@gmai.com', 'pratiii2@hotmail.com', msg)
    print("Email has been sent")
    server.quit()


check_price()












#print(price)