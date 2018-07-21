import time
import random

from flask_restful import Resource, marshal
from flask_login import login_required


class CryptoPriceResource(Resource):
    '''
    Provide an the basic price and an aggregation
    '''
    url = 'price'

    def get(self):
        response_rate = random.randint(0, 100)
        sleep_time = random.randint(10, 30)
        time.sleep(sleep_time)

        if response_rate >= 80:
            return {
                'data': {
                    'btc': 633.23 
                },
                'err': ''
            }, 200
        else:
            return {
                'err': 'Enhance your calm.'
            }, 420
