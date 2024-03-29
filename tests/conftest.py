"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import logging
import os

import pytest
from app import create_app, User
from app.db import db

@pytest.fixture()
def application():
    """This makes the app"""
    #you need this one if you want to see whats in the database
    #os.environ['FLASK_ENV'] = 'development'
    #you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'

    application = create_app()

    with application.app_context():
        db.create_all()
        #this below mention code helps to pass the test where csrf token is missing
        application.config['WTF_CSRF_ENABLED'] = False
        yield application
        db.session.remove()
        #drops the database tables after the test runs
        #db.drop_all()

@pytest.fixture()
def add_user(application):
    with application.app_context():
        #new record
        user = User('keith@webizly.com', 'testtest')
        db.session.add(user)
        db.session.commit()

@pytest.fixture()
def add_user(application):
    with application.app_context():
        #new record for one other user
        user = User('parth@webizly.com', 'testtest')
        db.session.add(user)
        db.session.commit()

@pytest.fixture()
def add_user(application):
    with application.app_context():
        #new record for second other user
        user = User('parth@test.com', 'testtest')
        db.session.add(user)
        db.session.commit()



@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()
