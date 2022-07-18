import yfinance as yf
from flask import (
    Blueprint, request
)

bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@bp.route('/history', methods=(['POST']))
def history():
    ticker = request.json.get('ticker', '')
    start = request.json.get('start', '')
    end = request.json.get('end', '')
    if valid_request():
        history = yf.Ticker(ticker).history(
            start=start, end=end, interval='1d',
        )
        history.index = history.index.strftime('%Y-%m-%d')
        return history.to_dict()

    return {'message': 'Invalid parameters'}, 401


def valid_request():
    # TODO: implement validation
    return True
