import logging

from app.MoneysParser import MoneysParser
from app.CriptoParse import CriptoParser
from app.Config import Config

config = Config()

class RestService:
    def __init__(self):
        self.moneys = MoneysParser(config.moneys_href)
        self.cripto = CriptoParser(config.crypto_href)
        self.cache_moneys = {}
        self.cache_crypto = {}

    def get_moneys(self) -> dict[str, float]:
        res = self.moneys.parse()
        if res is None:
            logging.warning('Failed to parse moneys')
        else:
            logging.debug(f'Successfully parsed moneys {res}')
            self.cache_moneys = res
        self.cripto.set_usdc(self.cache_moneys)
        return self.cache_moneys

    def get_crypto(self) -> dict[str, float]:
        res = self.cripto.parse()
        if res is None:
            logging.warning('Failed to parse crypto')
        else:
            logging.debug(f'Successfully parsed crypto {res}')
            self.cache_crypto = res
        return self.cache_crypto