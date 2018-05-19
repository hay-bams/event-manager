import pytest

from app import create_app
from app import app_config
import os
import tempfile

db_fd, db = tempfile.mkstemp()
class TestingConfig():
    ''' configuration for test '''
    TESTING = True
    SECRET_KEY = 'our event secret is only known by us'
    SQLALCHEMY_DATABASE_URI = db
    DEBUG = True

@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    # params = {
    #     'DEBUG': False,
    #     'TESTING': True,
    # } could have used this custom set up

    _app = create_app(config_class=TestingConfig)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()

    # os.close(db_fd)
    # os.unlink(db)
