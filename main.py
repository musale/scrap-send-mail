"""Main file."""
import email.message
import smtplib
from string import Template

import requests
from bs4 import BeautifulSoup

from utils.variables import SENDER_EMAIL, SENDER_EMAIL_PASSWORD, headers

SEND_TO = ['musale@focusmobile.co']
MESSAGE_CONTAINER = email.message.Message()
MESSAGE_CONTAINER['Subject'] = "UPDATES"
MESSAGE_CONTAINER['From'] = SENDER_EMAIL
MESSAGE_CONTAINER.add_header('Content-Type', 'text/html')


def main():
    """Run this function to do stuff."""
    url = "http://optimetriks.breezy.hr/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('h2')
    image = soup.img.get('src')
    substitute_ = {
        'data': "".join(str(x) for x in data),
        'image': image,
        'url': url
    }
    html_data = open('utils/email.txt')
    src = Template(html_data.read())
    MESSAGE_CONTAINER.set_payload(src.safe_substitute(substitute_))

    # setup the email server,
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # add my account login name and password,
    server.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)

    # send the email
    server.sendmail(SENDER_EMAIL, SEND_TO, MESSAGE_CONTAINER.as_string())
    # disconnect from the server
    server.quit()


if __name__ == '__main__':
    main()
