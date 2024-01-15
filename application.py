from flask import Flask, render_template, request, url_for
import requests

application = Flask(__name__)

@application.route('/')
def say_hello():
    return render_template('index.html', word_data1="blank", word_data2="blank", input_data="blank")

@application.route('/handle_get', methods=['GET'])
def handle_get():
    stock_data = request.args['inputBox'];
    info1 = requests.get("https://api.tiingo.com/tiingo/daily/" + stock_data + "?token=dee06621be72c181ee60cc14cc10dbca4a07c197", headers=headers)
    info2 = requests.get("https://api.tiingo.com/iex/" + stock_data + "?token=dee06621be72c181ee60cc14cc10dbca4a07c197", headers=headers)
    return render_template('index.html', word_data1=info1.json(), word_data2=info2.json(), input_data=stock_data)

headers = {
        'Content-Type': 'application/json'
        }