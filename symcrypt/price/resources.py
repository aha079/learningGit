from flask_restful import Resource, marshal

from flask_login import login_required


class PriceResource(Resource):
    '''
    Provide an the basic price and an aggregation
    '''
    
    @login_required
    def get(self):
        pass
