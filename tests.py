# def sortBy(posts, field, direction):
#         fields = {'id', 'reads', 'likes', 'popularity'}

#         if field not in fields:
#             return False
#         else:
#             if direction != 'desc':
#                 sorted_posts = sorted(posts, key= lambda x: x[field])
#             else:
#                 sorted_posts = sorted(posts, key= lambda x: x[field], reverse = True)
#         return sorted_posts

# posty = [{'author': 'Rylee Paul', 'authorId': 9, 'id': 1, 'likes': 960, 'popularity': 0.13, 'reads': 50361, 'tags': ['tech', 'health']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 3, 'likes': 425, 'popularity': 0.68, 'reads': 11381, 'tags': ['startups', 'health']}, {'author': 'Bryson Bowers', 'authorId': 6, 'id': 5, 'likes': 44, 'popularity': 0.57, 'reads': 94293, 'tags': ['startups', 'health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 7, 'likes': 499, 'popularity': 0.93, 'reads': 95434, 'tags': ['science', 'health']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 10, 'likes': 853, 'popularity': 0.6, 'reads': 35913, 'tags': ['science', 'health', 'history']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 17, 'likes': 527, 'popularity': 0.88, 'reads': 52454, 'tags': ['science', 'health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 27, 'likes': 324, 'popularity': 0.98, 'reads': 73428, 'tags': ['health']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 32, 'likes': 992, 'popularity': 0.84, 'reads': 32530, 'tags': ['health']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 34, 'likes': 670, 'popularity': 0.24, 'reads': 65450, 'tags': ['health']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 36, 'likes': 709, 'popularity': 0.08, 'reads': 65277, 'tags': ['health', 'design']}, {'author': 'Adalyn Blevins', 'authorId': 11, 'id': 37, 'likes': 107, 'popularity': 0.55, 'reads': 35946, 'tags': ['tech', 'health', 'history']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 41, 'likes': 715, 'popularity': 0.69, 'reads': 47876, 'tags': ['design', 'health']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 47, 'likes': 852, 'popularity': 0.25, 'reads': 72023, 'tags': ['culture', 'health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 48, 'likes': 201, 'popularity': 0.57, 'reads': 13867, 'tags': ['politics', 'health']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 50, 'likes': 898, 'popularity': 0.96, 'reads': 4923, 'tags': ['health', 'history']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 52, 'likes': 602, 'popularity': 0.26, 'reads': 76359, 'tags': ['science', 'health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 53, 'likes': 62, 'popularity': 0.62, 'reads': 68047, 'tags': ['politics', 'health']}, {'author': 'Elisha Friedman', 'authorId': 8, 'id': 56, 'likes': 319, 'popularity': 0.49, 'reads': 96864, 'tags': ['design', 'health', 'culture']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 60, 'likes': 52, 'popularity': 0.07, 'reads': 39800, 'tags': ['health']}, {'author': 'Ahmad Dunn', 'authorId': 7, 'id': 61, 'likes': 108, 'popularity': 0.51, 'reads': 5103, 'tags': ['startups', 'health']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 66, 'likes': 224, 'popularity': 0.05, 'reads': 20532, 'tags': ['health']}, {'author': 'Trevon Rodriguez', 'authorId': 5, 'id': 67, 'likes': 903, 'popularity': 0.71, 'reads': 26815, 'tags': ['health', 'history']}, {'author': 'Kinley Crosby', 'authorId': 10, 'id': 70, 'likes': 632, 'popularity': 0.6, 'reads': 15459, 'tags': ['startups', 'health']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 71, 'likes': 321, 'popularity': 0.69, 'reads': 29331, 'tags': ['culture', 'health', 'politics']}, {'author': 'Lainey Ritter', 'authorId': 1, 'id': 76, 'likes': 122, 'popularity': 0.01, 'reads': 75771, 'tags': ['tech', 'health', 'politics']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 78, 'likes': 539, 'popularity': 0.45, 'reads': 13562, 'tags': ['health']}, {'author': 'Zackery Turner', 'authorId': 12, 'id': 91, 'likes': 455, 'popularity': 0.19, 'reads': 90395, 'tags': ['science', 'health']}, {'author': 'Rylee Paul', 'authorId': 9, 'id': 92, 'likes': 203, 'popularity': 0.49, 'reads': 82099, 'tags': ['health']}, {'author': 'Jon Abbott', 'authorId': 4, 'id': 95, 'likes': 985, 'popularity': 0.42, 'reads': 55875, 'tags': ['politics', 'tech', 'health', 'history']}]
# field = 'popularity'

# print(sortBy(posty, field, 'desc'))

def findRestaurant(list1, list2):
    l1_dict = {list1[i]: i for i in range(len(list1))}
    min_sum = len(list1) + len(list2) - 2
    least = None
    for i in range(len(list2)):
        if list2[i] in l1_dict:
            if i + l1_dict[list2[i]] < min_sum:
                min_sum = i + l1_dict[list2[i]]
                least = list2[i]
    return least

one = ["Shogun","Tapioca Express","Burger King","KFC"]
two = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(one,two))