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
        r = session.get(url=self.__href, headers=headers)
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
        tr = data.find("table").find_all("tr")
        td = [el.find_all("td")[2:4] for el in tr]
        for el in td:
            if len(el) < 2: continue
            name = el[0].text
            cost = float(el[1].text.replace(".", "").replace(",","."))
            crypto[name] = self.__usdc * cost
        return crypto