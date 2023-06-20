"""Greet App"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Returns weclome"""
    return 'welcome'

@app.route('/welcome/home')
def say_weclome_home():
    """Returns welcome home"""
    return 'weclome home'

@app.route('/welcome/back')
def say_welcome_back():
    """Returns welcome back"""
    return 'welcome back'