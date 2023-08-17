import json
import smtplib
import urllib.request
from bs4 import BeautifulSoup
from email.message import EmailMessage
from datetime import datetime

log = ""

def checkAvialability(url, phrase):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html-parser')

        if phrase in soup.text:
            return False
        return True
    except:
        log +=  "Error parsing the website"



    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, features='html.parser')

    if phrase in soup.text:
        return False
    return True


def main():
    url = "https://www.amazon.in/dp/B0C7L17G91/ref=QAHzEditorial_en_IN_5?pf_rd_r=E4P5JXD6VRKY88NMK2JR&pf_rd_p=102c0538-cc6a-417d-917f-306869881c2c&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_t=&pf_rd_i=2563504031&th=1"
    phrase = "Maxima Fusion 1.96 HD Display smart watch"
    avialable = checkAvialability(url, phrase)

    if avialable:

        with open('config.json') as file:
            config = json.load(file)
            username = config['username']
            password = config['password']
            fromAddress = config['fromAddress']
            toAddress = config['toAddress']

        msg = EmailMessage()
        msg['Subject'] = "Maxima Fusion smart watch is in stock"
        msg['From'] = config['fromAddress']
        msg['To'] = config['toAddress']
        msg.set_content("It seems that there is Maxima Fusion smart watch avialable at " + url)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)

        server.send_message(msg)
        server.quit()

if __name__ == '__main__':
    main()