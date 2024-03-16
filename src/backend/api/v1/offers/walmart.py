import os
import capsolver
from .models import Offer, OfferRequest
from urllib import parse
import requests
from bs4 import BeautifulSoup
import re


def solve_captcha(site_key: str, url: str) -> dict[str, str]:
    capsolver.api_key = os.getenv('CAPSOLVER_API_KEY')

    return capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteURL": url,
        "websiteKey": site_key,
    })


def get_walmart_offer(url: str, data: OfferRequest) -> Offer:
    if data.broken or data.damaged:
        condition = 95
    elif data.working:
        condition = 94
    else:
        return Offer(site_name="walmart", amount=0, url=url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    selected_component = None
    if component_element := soup.find('div', text=re.compile('Unlocked')):
        selected_component = component_element.attrs.get('id').split('-')[1]

    params = parse.parse_qs(parse.urlsplit(url).query)  #: 'https://walmart.cexchange.com/Online/Cart/BeginAppraisal-ShowAppraisalForm.rails?pcat=2&man=2&modelId=81651&forcelayout=true'

    recaptcha_solution = solve_captcha('6LfRGxAUAAAAABU39qA1I-OhMbgOGGxPhlNk_x4p', url)

    headers = {
        "User-Agent": recaptcha_solution['userAgent']
    }

    recaptcha_token = recaptcha_solution['gRecaptchaResponse']

    data = {
        'Model.ModelId': params['modelId'],
        'pcat': params['pcat'],
        'SelectedPromoProduct': '',
        'ApplyPromoAdditionalDataTextBox1': '',
        'ApplyPromoAdditionalDataTextBox2': '',
        'ApplyPromoAdditionalDataTextBox1ValidatorMessage': '',
        'ApplyPromoAdditionalDataTextBox2ValidatorMessage': '',
        'TheConditions': 'on',
        'Condition': str(condition),
        'AccessoryId-1526': 'no',
        'g-recaptcha-response': recaptcha_token,
    }

    if component_element:
        data['SelectedComponent'] = selected_component

    response = requests.post(
        'https://walmart.cexchange.com/Online/Cart/BeginAppraisal-UpdatePrice.rails',
        headers=headers,
        data=data,
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    dollars = soup.find('span', {'class': 'AppraisalPrice-bucks'})
    cents = soup.find('span', {'class': 'AppraisalPrice-cents'})

    if dollars and cents:
        amount = float(dollars.text) + float(cents.text) / 100
        return Offer(site_name="walmart", amount=amount, url=url)

    return Offer(site_name="walmart", amount=0, url=url)
