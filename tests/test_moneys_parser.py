import pytest
from pytest_mock import MockerFixture
from bs4 import BeautifulSoup as bs

from app.MoneysParser import MoneysParser


class TestMoneyParser:
    mp = MoneysParser("")

    def data_ser(self, data):
        return [bs(el, "html.parser") for el in data]

    def test_get_curs(self):
        inp , out = (["<td>710</td>", "<td>ZAR</td>", "<td>10</td>", "<td>Рэндов</td>", "<td>53,6614</td>"], ("ZAR", 5.36614))
        assert self.mp.get_curs(self.data_ser(inp)) == out

    def test_parse(self, response_data, parse_data, mocker: MockerFixture):
        mocker.patch.object(self.mp, "get_request", return_value=response_data)
        res = self.mp.parse()
        assert res == parse_data

    def test_parse_errors(self, response_data, parse_data, mocker: MockerFixture):
        mocker.patch.object(self.mp, "get_request", return_value=response_data)
        curs = mocker.patch.object(self.mp, "get_curs", return_value=("A", 1.))
        self.mp.parse()
        assert len(response_data.find_all("tr"))-1 == curs.call_count