import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

#print(soup.prettify())

d1 = soup.find_all('div',{'class': '_3O0U0u'})
#print(BeautifulSoup.prettify(d1[0]))
container = d1[0]
#print(container.div.img['alt'])

price = container.find_all('div',{'class':'col col-5-12 _2o7WAb'})
#print(price[0].text)

rating = container.find_all('div',{'class':'niH0FQ'})
#print(rating[0].text)

filename = "product.csv"

f = open(filename,'w')
headers = "product_name,pricing,ratings\n"

f.write(headers)

for container in d1:
    product_name = container.div.img['alt']

    price_container = container.find_all('div',{'class':'col col-5-12 _2o7WAb'})
    price =  price_container[0].text.strip()

    rating_container =  container.find_all('div',{'class':'niH0FQ'})
    rating = rating_container[0].text



    trim_price = ''.join(price.split(','))
    rm_price = trim_price.split('₹')
    add_rp_price = "Rs."+rm_price[1]
    split_price = add_rp_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(' ')
    final_rating = split_rating[0]
    print(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")
    f.write(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")
    #print('price '+final_price)
    #print('ratings ' +final_rating)

    #print(product_name.replace(',','|')+","+final_price+","+final_rating+"\n")
f.close()