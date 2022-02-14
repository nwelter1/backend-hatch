from re import T
from flask import Blueprint
import requests

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/ping', methods=['GET'])
def ping():
    ping = requests.get('https://api.hatchways.io/assessment/blog/posts?tag=tech').status_code
    print(ping)
    if ping == 200:
        return {'success':True}, 200
    return {'success': False}

@api.route('/posts/<tags>', methods=['GET'])
@api.route('/posts/<tags>/<sortBy>/<direction>', methods=['GET'])
def posts(tags, sortBy = None, direction = None):
    print(tags)
    if not sortBy and not direction:
        res = requests.get(f'https://api.hatchways.io/assessment/blog/posts?tag={tags}')
        return (res.json())
    elif sortBy:
        if sortBy != 'id' or sortBy != 'reads' or sortBy != 'likes' or sortBy != 'popularity':
            return {'message': 'Invalid Syntax'}, 401
        queries = []
        for tag in tags:
            pass
        
        #posts = requests.get('https://api.hatchways.io/assessment/blog/posts?tag=tech')
    elif not direction:
        pass
    else:
        pass
