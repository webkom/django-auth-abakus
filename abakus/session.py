import requests

from . import __version__


class LegoSession(requests.Session):

    def __init__(self):
        super(LegoSession, self).__init__()
        self.headers.update({
            'Accept-Charset': 'utf-8',
            'Content-Type': "application/json",
            'User-Agent': 'django-abakus-auth/{version}'.format(version=__version__),
        })
