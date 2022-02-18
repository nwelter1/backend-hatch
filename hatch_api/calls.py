from flask import json, jsonify, request
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
            return 'asc'
        return direction

    def tagList(self, tags):
        return tags.split(',')
    
    def getPostsByTag(self, tag):
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
        print(self.direction, 'hello')
        if self.direction != 'asc' and self.direction != 'desc':
            return False
        return True

    def checkSortField(self):
        fields = {'id', 'reads', 'likes', 'popularity'}
        if self.sort_by not in fields:
            return False
        return True

    def getAllPosts(self):
        posts = []
        for tag in self.tags:
            tag_posts = self.getPostsByTag(tag)
            for post in tag_posts:
                posts.append(post)
        unique_posts = self.removeDuplicates(posts)
        sorted_posts = self.sortByField(unique_posts)
        return jsonify(sorted_posts), 200
    
    def removeDuplicates(self, posts):
        seen = set()
        clean_posts = []
        for post in posts:
            if post['id'] not in seen:
                seen.add(post['id'])
                clean_posts.append(post)
        return clean_posts



