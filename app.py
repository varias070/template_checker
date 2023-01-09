from flask import Flask
from tinydb import TinyDB
from test_requests import test

app = Flask(__name__)
db = TinyDB('templates.json')
test()
