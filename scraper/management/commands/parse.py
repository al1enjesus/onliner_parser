from fake_useragent import UserAgent
import requests
import logging

from django.core.management.base import BaseCommand
from scraper.models import Product

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')


class Spider:
    types = ("videocard", "tv", "mobile", "notebook")

    def __init__(self, products_type="videocard"):
        if products_type not in Spider.types:
            raise Exception("This type of product is not provided.")
        self.type = products_type
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': str(UserAgent().random)
        }

    def parse_last_page_number(self) -> int:
        last_url = "https://catalog.onliner.by/sdapi/catalog.api/search/{}/?page=9999999999".format(self.type)
        res = self.session.get(url=last_url).json()
        return res["page"]["last"]

    def parse_page(self, page: int) -> str:
        url = "https://catalog.onliner.by/sdapi/catalog.api/search/{}/?page={}".format(self.type, page)
        res = self.session.get(url=url).json()
        return res

    def parse_products(self, res):
        products = res['products']
        for product in products:
            if product['prices']:
                name = product['full_name']
                min_price = product['prices']['price_min']['amount']
                max_price = product['prices']['price_max']['amount']
                url = product['html_url']

                try:
                    p = Product.objects.get(url=product['html_url'])
                    p.name = name
                    p.min_price = min_price
                    p.max_price = max_price
                    p.url = url
                    p.type = self.type
                    print("Changed product {}".format(name))
                except Product.DoesNotExist:
                    p = Product(
                        name=name,
                        min_price=min_price,
                        max_price=max_price,
                        url=url,
                        type=self.type
                    ).save()

    def parse_pages(self):
        last_page_number = self.parse_last_page_number()
        for _ in range(1, last_page_number + 1):
            res = self.parse_page(_)
            self.parse_products(res)

    def run(self):
        self.parse_pages()


class Command(BaseCommand):
    help = 'Парсинг onliner'

    def handle(self, *args, **options):
        p = Spider("notebook")
        p.run()
