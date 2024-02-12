# import requests
# from pprint import pprint
# import urllib.request
# import random
#
# url = "https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/data"
# post = "https://pin.it/5dUupCPqq"
# querystring = {"url": post}
#
# headers = {
#             "X-RapidAPI-Key": "f5c031158amsh3e427efcf8451d8p151c85jsn9ff8191549bc",
#             "X-RapidAPI-Host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com"
# }
# a = "qwertaysjlf"
# response = requests.get(url, headers=headers, params=querystring)
# data = response.json()
# img_url = data["data"]["images"]["564x"]["url"]
# img_name = ""
# for i in random.sample(a, 5):
#     img_name += i
#
# # img_name = data["data"]["images"]["564x"]["width"]
# urllib.request.urlretrieve(img_url, f'{img_name}.jpg')
#
#
# pprint(response.json())


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Xabar jo'natiladigan email manzili
to_email = "abdullayevabduaxad571@gmail.com"
# Jo'natuvchi email manzili
from_email = "kkadyr039@gmail.com"
# Jo'natuvchi email paroli
email_password = "582#post"

# Xabar tarkibi
subject = "Test Xabar"
body = "Bu xabar Python orqali yuborilgan test xabari."
message = MIMEMultipart()
message.attach(MIMEText(body, "plain"))
message["Subject"] = subject
message["From"] = from_email
message["To"] = to_email

# SMTP serverini sozlash
smtp_server = "localhost"
smtp_port = 25

# SMTP serveriga ulanish
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Ulanishni boshlash
        server.starttls()
        # Login qilingan holda ulanish
        server.login(from_email, email_password)
        # Xabarni yuborish
        server.sendmail(from_email, to_email, message.as_string())
        print("Xabar muvaffaqiyatli jo'natildi.")
except Exception as e:
    print(f"Xabar yuborishda xatolik: {e}")





