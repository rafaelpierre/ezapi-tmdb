import requests

from .certifications import CertificationsMixin
from .changes import ChangesMixin
from .companies import CompaniesMixin
from .configuration import ConfigurationMixin
from .discover import DiscoverMixin
from .genres import GenresMixin
from .keywords import KeywordsMixin
from .movies import MoviesMixin
from .people import PeopleMixin
from .reviews import ReviewsMixin
from .trending import TrendingMixin
from .tv import TVsMixin

mixins = [
    CertificationsMixin,
    ChangesMixin,
    CompaniesMixin,
    ConfigurationMixin,
    DiscoverMixin,
    GenresMixin,
    KeywordsMixin,
    MoviesMixin,
    PeopleMixin,
    ReviewsMixin,
    TrendingMixin,
    TVsMixin,
]


class TMDb(*mixins):
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json;charset=utf-8"})

    def make_request(self, method, url, params, payload=None):
        params.update({"api_key": self.api_key})
        return self.session.request(method, url, params=params, json=payload)
