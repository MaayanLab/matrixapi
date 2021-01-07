import datetime
import time
import tornado.escape
import tornado.ioloop
import tornado.web
import os
import io
import string
import random
import requests
import hashlib
import base64
import hmac
import uuid
import boto
from dateutil import parser
import threading
import re
import h5py

root = os.path.dirname(__file__)


class CreateUserHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        username = self.get_argument('username', True)
        password = self.get_argument('password', True)
        firstname = self.get_argument('firstname', True)
        lastname = self.get_argument('lastname', True)
        email = self.get_argument('email', True)
        invitationKey = self.get_argument('invitationKey', True)
        
        if invitationKey == 'charon2018':
            createUser(username, password, firstname, lastname, email, self)
        else:
            response = { 'action': 'create user',
                 'task': username,
                 'status': 'error',
                 'message': 'invitationKey needed'}
            self.write(response)

class MoveHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        
        response = { 'bestmove': bestmove[len(bestmove)-1],
                     'other':  "list of stuff",
                     'rating': score[len(score)-1] }
        
        self.write(response)
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        response = { 'version': '1',
                     'last_build':  datetime.date.today().isoformat() }
        self.write(response)
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        response = { 'version': '1',
                     'last_build':  datetime.date.today().isoformat() }
        self.write(response)


application = tornado.web.Application([
    (r"/version", VersionHandler),
    (r"/chessapi/bestmove", MoveHandler),
    (r"/chessapi/(.*)", tornado.web.StaticFileHandler, dict(path=root))
])


if __name__ == "__main__":
    application.listen(5000)
tornado.ioloop.IOLoop.instance().start()