import logging
from time import sleep

import requests as rq
from bs4 import BeautifulSoup as bs

class CriptoParser:
    def __init__(self, href: str = ""):
        self.__href = href
        self.__usdc = 80

    def get_request(self, p: int = 1):
        headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
        session = rq.Session()
        r = rq.get(url=self.__href, headers=headers)
        # print(r.headers)
        # print(r.text)
        if r.status_code != 200:
            logging.error(f"can`t connect to cripto, status code is {r.status_code}")
        return bs(r.text, "html.parser")

    def get_curs(self, num) -> float:
        c = str(num.text).replace(",","")[1:]
        return float(c)

    def set_usdc(self, money: dict[str, float]) -> None:
        self.__usdc = money["USD"]
        logging.info(f"set usdc: {money["USD"]}")

    def parse(self) -> dict[str, float] | None:
        crypto = {}
        data = self.get_request()
        data = data.find_all("button")
        logging.debug(f"crypto parse: {data}")
        if len(data)>3:
            kol = int(data[-2].text)
        else:
            logging.warning("connection blocked")
            return None
        try:
            for i in range(kol):
                data = self.get_request(i).find_all("div", {"class": "css-1ydqfmf"})
                for el in data:
                    name = el.find("div", {"class": "subtitle3 text-t-primary css-vurnku"})
                    cost = el.find("div", {"class": "body2 items-center css-18yakpx"})
                    crypto[name.text] = self.get_curs(cost) * self.__usdc
        except Exception as e:
            crypto = None
            logging.error(f"crypto parse error:\n\t{e}")
        return crypto