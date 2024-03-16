from .models import Offer, OfferRequest
import requests
from urllib import parse


def get_bestbuy_offer(url: str, data: OfferRequest) -> Offer:
    headers = {
        'accept': 'application/madness+json, text/plain, */*',
        'referer': 'https://tradein.bestbuy.com/client/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    params = parse.parse_qs(parse.urlsplit(url).query)

    params = {
        'sku': params['sku'][0],
        'crackedscreen-mob-1': 'No' if not data.damaged else 'Yes',
        'cellphone-condition2': 'Good' if not data.broken else 'Broken',
        'cell-phones-10': 'Yes'
    }

    response = requests.get('https://tradein.bestbuy.com/catalog/products/appraisal', params=params,
                            headers=headers)

    if response.status_code != 200:
        return Offer(site_name="bestbuy", amount=0)

    data = response.json()
    return Offer(site_name="bestbuy", amount=data.get('appraisalValue', 0))
