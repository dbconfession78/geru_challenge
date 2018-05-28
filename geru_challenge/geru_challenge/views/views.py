from pyramid.view import (
    view_config,
    view_defaults
)
from datetime import datetime
from .page_request import PageRequest
import requests
from random import sample
from pyramid.session import SignedCookieSessionFactory
from uuid import uuid4
from ..models.engine.db_storage import DBStorage


@view_defaults(renderer='templates/index.jinja2')
class APIRequestManagaer:
    def __init__(self, request):
        """
        __init__ - initializes an instance of the API class
        """
        self.api_url = "https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes"
        self.api_messages = [" is not a valid quote id.",
                             "unable to connect to api."]
        self.n = None
        self.session_factory = SignedCookieSessionFactory("Ican'ttellyoumysecretnowcanI?")
        self.request = request
        self.session = None
        self.storage = DBStorage()
        
    @view_config(route_name='get_quotes')
    def get_quotes(self):
        """
        get_quotes - api request for all quotes from 'Zen of Python'
        :Return: a dictionary with either the requested quote or an api message
        """
        self.handle_session()
        r = requests.get(self.api_url)
        if r.status_code == 200:
            dct = r.json()
            return {"dct": dct}
        else:
            return {"quotes": ["Unable to retrieve quotes"]}

    @view_config(route_name='get_quote')
    def get_quote(self):
        """
        get_quote - api request for quote based on input quote index, 'n'
        :n: api quote index
        :Return: dictionary with either the requested quote or error message
        """
        self.handle_session()
        self.n = self.request.matchdict.get('quote_num')
        # self.n = None
        r = requests.get(self.api_url)
        if r.status_code == 200:
            quotes = r.json()["quotes"]
            _len = len(quotes)
            if not self.n.isnumeric():
                if self.n == "random":
                    self.n = sample(range(1, _len+1), 1)[0]
            else:
                self.n = int(self.n)

#            self.n = n
            if type(self.n) != int:
                val = "{}".format(self.api_messages[0])
                return {"quote": "{}".format(val)}

            val = quotes[self.n-1] if self.n > 0 and self.n <= _len else \
                self.api_messages[0]
        else:
            val = self.api_messages[1]
        dct = {"quote": "{}".format(val), "n": self.n}
        return {"dct": dct}

    def handle_session(self):
        """
        handle_session - stores session info in db
        :param request: session request
        :return: None
        """
        id = self.request.session.get('id')
        if not id:
            id = str(uuid4())
            self.request.session['id'] = id
            print("new session ID: {}".format(id))
        else:
            print("updated existing ID: {}".format(id))

        req_url = self.request.path_url
        new_request = PageRequest(session_id=self.request.session['id'],
                                  datetime = datetime.now(),
                                  request = req_url)
        self.storage.new(new_request)
        self.storage.save()


    @view_config(route_name='home')
    def home(self):
        self.handle_session()
        return {'name': 'geru_quotes_api_v3'}
    
