from dataclasses import replace

import pytest
from pytest_mock import MockerFixture

from app.MainController import rest_service


class TestController:
    def data_to_str(self, data: dict[str, float]) -> str:
        return "{" + ",".join(f"\"{k}\":{v}" for k, v in data.items()) + "}"

    def test_get_all(self, cli, test_data_1: dict[str, float], test_data_2: dict[str, float], mocker: MockerFixture):
        mn = mocker.patch.object(rest_service, 'get_moneys', return_value=test_data_1)
        cr = mocker.patch.object(rest_service, 'get_crypto', return_value=test_data_2)
        r = cli.get("/all")
        assert r.status_code == 200
        assert r.text == self.data_to_str({**test_data_1, **test_data_2})
        assert mn.call_count == 1
        assert cr.call_count == 1

    def test_get_moneys(self, cli, test_data_1: dict[str, float], mocker: MockerFixture):
        mn = mocker.patch.object(rest_service, 'get_moneys', return_value=test_data_1)
        r = cli.get("/moneys")
        assert r.status_code == 200
        assert r.text == self.data_to_str(test_data_1)
        assert mn.call_count == 1

    def test_get_crypto(self, cli, test_data_2: dict[str, float], mocker: MockerFixture):
        cr = mocker.patch.object(rest_service, 'get_crypto', return_value=test_data_2)
        r = cli.get("/crypto")
        assert r.status_code == 200
        assert r.text == self.data_to_str(test_data_2)
        assert cr.call_count == 1