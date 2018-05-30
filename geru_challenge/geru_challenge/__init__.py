from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from wsgiref.simple_server import make_server


def main(global_config=None, **settings):
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
        config.add_static_view(name='static', path='geru_challenge:static')

        config.scan(".views")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
    return config.make_wsgi_app()
