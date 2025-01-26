import pytest
from fastapi.testclient import TestClient
from bs4 import BeautifulSoup as bs

from main import app


@pytest.fixture(scope='session')
def ap():
    return app

@pytest.fixture(scope='session')
def cli(ap):
    return TestClient(app=ap)

@pytest.fixture(scope='session')
def test_data_1() -> dict[str, float]:
    return {'AUD':62.0633, 'AZN':57.8021, 'AMD':0.246293, 'THB':2.90867, 'BYN':28.7766, 'BGN':52.2712}

@pytest.fixture(scope='session')
def test_data_2() -> dict[str, float]:
    return {'AU':62.0633, 'AZ':57.8021, 'AM':0.246293, 'TH':2.90867, 'BY':28.7766, 'BG':52.2712}

@pytest.fixture(scope='session')
def response_data():
    with open('response.txt', 'r', encoding="utf-8") as f:
        return bs(str(f.read()), "html.parser")

@pytest.fixture(scope='session')
def parse_data():
    return {'AUD': 62.0633, 'AZN': 57.8021, 'AMD': 0.246293, 'THB': 2.90867, 'BYN': 28.7766, 'BGN': 52.2712, 'BRL': 16.5438, 'KRW': 0.0683763, 'HKD': 12.6384, 'UAH': 2.341, 'DKK': 13.7031, 'AED': 26.7566, 'USD': 98.2636, 'VND': 0.00403961, 'EUR': 103.187, 'EGP': 1.95398, 'PLN': 24.49, 'JPY': 0.628927, 'INR': 1.13875, 'CAD': 68.3763, 'QAR': 26.9955, 'GEL': 34.3255, 'MDL': 5.2714799999999995, 'NZD': 55.7449, 'TMT': 28.0753, 'NOK': 8.71518, 'RON': 20.5607, 'IDR': 0.0060373300000000005, 'ZAR': 5.36614, 'XDR': 128.0611, 'RSD': 0.877198, 'SGD': 72.7879, 'KGS': 1.12365, 'TJS': 8.9763, 'KZT': 0.188093, 'TRY': 2.75839, 'UZS': 0.00757089, 'HUF': 0.251984, 'GBP': 121.1001, 'CZK': 4.06485, 'SEK': 8.91429, 'CHF': 108.3153, 'CNY': 13.5101}
