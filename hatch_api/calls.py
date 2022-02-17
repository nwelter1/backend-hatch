from flask import json, request
import requests


class Call:
    def __init__(self, tags, sort_by, direction):
        self.tags = self.tagList(tags)
        self.sort_by = self.setSortyBy(sort_by)
        self.direction = self.setDirection(direction)
    
    def setSortyBy(self, sort_by):
        if not sort_by:
            return 'id'
        return sort_by

    def setDirection(self, direction):
        if not direction:
            return 'id'
        return direction

    def tagList(self, tags):
        return tags.split(',')
    
    def getPosts(self, tag):
        res = requests.get(f'https://api.hatchways.io/assessment/blog/posts?tag={tag}')
        return res.json()['posts']

    def sortByField(self, posts):
        field = self.sort_by
        if self.direction != 'desc':
            sorted_posts = sorted(posts, key= lambda x: x[field])
        else:
            sorted_posts = sorted(posts, key= lambda x: x[field], reverse = True)
        return sorted_posts
    
    # Error handling
    def checkSortDirection(self):
        print(self.direction)
        if self.direction != 'asc' and self.direction != 'desc':
            return False
        return True

    def checkSortField(self):
        fields = {'id', 'reads', 'likes', 'popularity'}
        if self.sort_by not in fields:
            return False
        return True



