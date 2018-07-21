from flask_restful import reqparse


crypto_price_parser = reqparse.RequestParser()
crypto_price_parser.add_argument(
    'currency', type=str, required=True, choise=['btc', 'eth'])
