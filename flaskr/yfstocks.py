import yfinance as yf
import csv
from flask import (
    Blueprint, request, current_app
)

bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@bp.route('/<ticker>/history', methods=(['GET']))
def history(ticker):
    start = request.args.get('start', '')
    end = request.args.get('end', '')
    if valid_request():
        history = yf.Ticker(ticker).history(
            start=start, end=end, interval='1d',
        )
        history.index = history.index.strftime('%Y-%m-%d')
        return history.to_dict()

    return {'message': 'Invalid parameters'}, 400


@bp.route('/list', methods=(['GET']))
def list():
    with open('flaskr/available_stocks.csv', mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)
        return {'stocks': [{'symbol': row[0], 'name': row[1], } for row in reader]}


def valid_request():
    # TODO: implement validation
    return True
