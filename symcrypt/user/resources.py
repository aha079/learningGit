from flask_restful import Resource, marshal

from symcrypt.user.models import UserModel
from flask_login import login_required
from symcrypt.user.validations import profile_parser


class ProfileResource(Resource):

    url = 'profile'

    @login_required
    def post(self):
        args = profile_parser.parse_args()
        u = UserModel.objects(username=args['username']).first()
        if not u:
            return {'err': 'User does not exist'}, 404

        return {
            'firstname': u.firstname,
            'lastname': u.lastname,
        }


# class ForgetPasswordResource(Resource):
#     pass
