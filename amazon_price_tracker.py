from pydoc import classname
import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = "https://www.amazon.in/Croma-Lithium-Polymer-Charging-CRSP10kPBA258901/dp/B09Z2XC3RG/ref=sr_1_2_sspa?crid=1UO9ZIVPVA6TP&keywords=power+bank+10000mah&qid=1654920455&sprefix=power%2Caps%2C1009&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE2RUlJQzhEQkdRUVcmZW5jcnlwdGVkSWQ9QTAzNzU4MTUyTUk5SzVNWFg2Ulo1JmVuY3J5cHRlZEFkSWQ9QTA1Mjg4OTA1NjEyRkdJRE5YRk4md2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
# to get user agent just search in google my user agent 
headers = {"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
def check_price():
      page = requests.get(URL,headers=headers)
      soup = BeautifulSoup(page.content,"html.parser")
      title = soup.find(id="title").get_text()
      price = soup.find(class_="a-price-whole").get_text()
      converted_price = int(price[0:3])
      print(converted_price)
      if(converted_price >= 500):
          print("should sent an email")
          send_email(title) 

def send_email(title):
     server = smtplib.SMTP("smtp.gmail.com",587)
     server.ehlo()
     server.starttls()
     server.ehlo()
     server.login("pokhrelanmol90@gmail.com","jwdojicnjzujseal")
     subject = f"Price fell down for {title} "
     body = f'Check the amazon link {URL} '
     msg = f"Subject:{subject}\n\n{body}"
     server.sendmail(
           "pokhrelanmol90@gmail.com",
           "anmolpokhrel46@gmail.com",
           msg
     )
     print("Email sent successfully")
     server.quit()

while True:
      send_email() 
      time.sleep(3600*24)