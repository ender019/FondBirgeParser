import logging
import requests as rq
from bs4 import BeautifulSoup as bs


class MoneysParser:
    def __init__(self, href):
        self.__href = href

    def get_request(self):
        r = rq.get(url=self.__href)
        if r.status_code != 200:
            logging.error("can`t connect to cripto")
        return bs(r.text, "html.parser")

    def get_curs(self, val) -> tuple[str, float]:
        c = str(val[4].text).replace(",",".")
        return val[1].text, float(c)/float(val[2].text)

    def parse(self):
        moneys = {}
        data = self.get_request()
        data = data.find("table").find_all("tr")
        logging.debug(f"moneys parse: {data}")
        try:
            for el in data:
                val = el.find_all("td")
                if len(val) == 0: continue
                res = self.get_curs(val)
                moneys[res[0]] = res[1]
        except Exception as e:
            moneys = None
            logging.error(f"money parse error:\n\t{e}")
        return moneys