from bs4 import BeautifulSoup
import smtplib
import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()

URL = "https://www.amazon.com/dp/B09MCVP94B/ref=sspa_dk_detail_right_aax_0?sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfcmlnaHRfc2hhcmVk&th=1"

MY_EMAIL = os.environ["MY_EMAIL"]

PASSWORD = os.environ["PASSWORD"]

headers = {"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 Edg/154.0.0.0" }

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")


#Get the product price and name from Amazon


price = str(soup.find("span", class_="a-price-whole"))

product_name = soup.find("span", id="productTitle", class_="a-size-large product-title-word-break")
new_price = re.split(r'>|<', price)

actual_price = new_price[2]

string_price = actual_price.replace(",", "")

amazon_price = int(float(string_price))

name = product_name.getText()

#
#Check if product price is less than $100, if that's the case, then send an email.

if amazon_price < 150000:
    print("Found an offer for you!")
    with smtplib.SMTP("smtp.gmail.com", 587) as send_message:
        send_message.starttls()
        send_message.login(MY_EMAIL, PASSWORD)
        message = f"Subject: Instant Pot Price Alert \n\n Hi there, I am writing to tell you that {name} is now #{amazon_price}. Rush to grab an Electric Pressure Cooker before it gets sold out."
        send_message.sendmail(MY_EMAIL, "folarinadeola295@gmail.com", msg=message.encode("utf-8"))

else:
    print("I am sorry. I couldn't find an offer for you!")