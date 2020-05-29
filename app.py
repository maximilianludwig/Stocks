from flask import Flask
from flask import render_template
from werkzeug.wrappers import Request, Response
import import_ipynb
from datetime import *

app = Flask(__name__)

@app.route('/')
def show_stocks():
    
    APPL = {"name": "Appel", "indicator":  "APPL", "decision": "buy"}
    DAX = {"name":"DAX","indicator": "^GDAXI","decision": "buy"}
    AMZN = {"name": "Amazon","indicator": "AMZN","decision": "sell"}
    MSFT = {"name": "Microsoft","indicator": "MSFT","decision": "nothing"}
    stock_indicators = [APPL, DAX, AMZN, MSFT]
    return render_template('Stocks.html', stocks=stock_indicators)  


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)    