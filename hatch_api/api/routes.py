from flask import Blueprint, request, jsonify
from hatch_api.calls import Call
import requests

api = Blueprint('api', __name__, url_prefix='/api')

# Route 1 - Ping
@api.route('/ping', methods=['GET'])
def ping():
    ping = requests.get('https://api.hatchways.io/assessment/blog/posts?tag=tech').status_code
    print(ping)
    if ping == 200:
        return {'success':True}, 200
    return {'failure': False}, 400


# Route 2 - API Posts
@api.route('/posts', methods=['GET'])
def posts():
    # Getting Params
    tags = request.args.get('tags')
    sortBy = request.args.get('sortBy')
    direction = request.args.get('direction')
    print(tags,sortBy,direction)
    # checking for invalid queries
    if not tags:
        return {'error':'Tags parameter is required'}, 400
    
    call = Call(tags, sortBy, direction)
    if not call.checkSortField():
        return {'error':'sortBy parameter is invalid'}, 400
    if not call.checkSortDirection():
        return {'error':'Sorting direction parameter is invalid'}, 400
    return call.getAllPosts()

# Old route below - realized it is easier to do this via OOP


# Route 2 - Accessing posts
# @api.route('/posts', methods=['GET'])
# def posts():
#     #instantiating empty list for posts return
#     posts = []
#     # Getting Params
#     tags = request.args.get('tags')
#     sortBy = request.args.get('sortBy')
#     direction = request.args.get('direction')
#     # 400 response if no required tags exist
#     if not tags:
#         return {'error': "The tag parameter is required!"}, 400
#     # get info for tags
#     tag_list = tags.split(',')
    
#     for tag in tag_list:
#         res = requests.get(f'https://api.hatchways.io/assessment/blog/posts?tag={tag}')
#         print(res.json())
#         return(res.json())
#         # posts.append(res.json())
#     return jsonify(posts)

    
#     elif sortBy:
#         fields = set('id', 'reads', 'likes', 'popularity')
#         if sortBy not in fields:
#             return {'message': 'Invalid Syntax'}, 401
#         queries = []
#         for tag in tags:
#             pass
        
#         #posts = requests.get('https://api.hatchways.io/assessment/blog/posts?tag=tech')
#     elif not direction:
#         pass
#     else:
#         pass



