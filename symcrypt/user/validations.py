from flask_restful import reqparse


profile_parser = reqparse.RequestParser()
profile_parser.add_argument(
    'username', type=str, required=True)
