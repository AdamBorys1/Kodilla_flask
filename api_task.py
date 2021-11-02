import requests
import csv
from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data = response.json()

data_dict = data[0]

data_rates = data_dict.get("rates")

with open("api_task.csv", "w") as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()

    currency_dict = {}
    code_list = []
    for items in data_rates:
        currency = items.get("currency")
        code = items.get("code")
        bid = items.get("bid")
        ask = items.get("ask")
        currency_dict.setdefault(code, ask)
        code_list.append(code)
        writer.writerow({"currency":currency, "code":code, "bid":bid, "ask":ask})


@app.route("/api_task", methods = ["GET", "POST"])
def api_task():
    if request.method == "GET":
        return render_template("api_task.html", items=items, currency=currency, currency_dict=currency_dict, code=code, ask=ask, code_list=code_list)
    elif request.method == "POST":
        request.form['currency']
        request.form['amount']
        result = currency * amount
        return render_template("result.html")


if __name__ == "__main__":
   app.run(debug=False)


