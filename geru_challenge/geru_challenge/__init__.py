from datetime import datetime
from waitress import serve
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.session import SignedCookieSessionFactory
from uuid import uuid4
from wsgiref.simple_server import make_server


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application."""
    session_factory = SignedCookieSessionFactory(
        "Ican'ttellyoumysecretnowcanI?")
    with Configurator() as config:
        config.include('pyramid_chameleon')
        config.include('pyramid_jinja2')
        config.set_session_factory(session_factory)
        config.add_route('home', '/')
        config.add_route('get_quotes', '/quotes')
        config.add_route('get_quote', '/quotes/{quote_num}')
        config.add_route('all_entries', '/api/session_requests')

        config.scan(".views")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever
    return config.make_wsgi_app()
