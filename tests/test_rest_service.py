from pytest_mock import MockerFixture

from app.CriptoParse import CriptoParser
from app.MainController import rest_service
from app.MoneysParser import MoneysParser


class TestRestService:
    def test_get_moneys(self, test_data_1: dict[str, float], mocker: MockerFixture) -> None:
        mn = mocker.patch.object(rest_service.moneys, 'parse', return_value=test_data_1)
        cr = mocker.patch.object(CriptoParser, 'set_usdc', return_value=None)
        res = rest_service.get_moneys()
        assert res == test_data_1
        assert mn.call_count == 1
        assert cr.call_count == 1

    def test_get_crypto(self, test_data_1: dict[str, float], mocker: MockerFixture):
        cr = mocker.patch.object(CriptoParser, 'parse', return_value=test_data_1)
        res = rest_service.get_crypto()
        assert res == test_data_1
        assert cr.call_count == 1