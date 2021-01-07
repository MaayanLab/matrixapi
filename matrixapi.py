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
from dateutil import parser
import threading
import re
import h5py as h5
import urllib.request

root = os.path.dirname(__file__)

base_name = os.environ['BASE_NAME']
matrix_url = os.environ['MATRIX_URL']
token = os.environ['TOKEN']

print("matrix: "+matrix_url)

urllib.request.urlretrieve(matrix_url, 'matrix.h5')
print("matrix loaded")


class ListRowID(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        data = tornado.escape.json_decode(self.request.body)
        f = h5.File("matrix.h5")
        ids = list(f["meta"]["rowid"])
        response = { 'rowID': [x.decode("UTF-8") for x in ids]}
        self.write(response)
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        f = h5.File("matrix.h5")
        ids = list(f["meta"]["rowid"])
        response = { 'rowID': [x.decode("UTF-8") for x in ids]}
        self.write(response)

class ListColID(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        data = tornado.escape.json_decode(self.request.body)
        f = h5.File("matrix.h5")
        ids = list(f["meta"]["colid"])
        response = { 'colID': [x.decode("UTF-8") for x in ids]}
        self.write(response)
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        f = h5.File("matrix.h5")
        ids = list(f["meta"]["colid"])
        response = { 'colID': [x.decode("UTF-8") for x in ids]}
        self.write(response)

class GetSlice(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        data = tornado.escape.json_decode(self.request.body)
        f = h5.File("matrix.h5")
        colids = list(f["meta"]["colid"])
        rowids = list(f["meta"]["rowid"])
        response = { 'colID': [x.decode("UTF-8") for x in ids]}
        self.write(response)

class GetCol(tornado.web.RequestHandler):
    def post(self):
        response = { 'version': '1',
                     'last_build':  datetime.date.today().isoformat() }
        self.write(response)
class GetRow(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        response = { 'version': '1',
                     'last_build':  datetime.date.today().isoformat() }
        self.write(response)
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
    (r"/"+base_name+"/version", VersionHandler),
    (r"/"+base_name+"/colid", ListColID),
    (r"/"+base_name+"/rowid", ListRowID),
    (r"/"+base_name+"/row", GetRow),
    (r"/"+base_name+"/col", GetCol),
    (r"/"+base_name+"/slice", GetSlice),
    (r"/"+base_name+"/(.*)", tornado.web.StaticFileHandler, dict(path=root))
])


if __name__ == "__main__":
    application.listen(5000)
tornado.ioloop.IOLoop.instance().start()