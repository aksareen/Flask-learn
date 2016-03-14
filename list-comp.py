DATA = [(u'Well', u"I'm well."), (u'Good', u"I'm good.")]

# list comp

posts_list_comp = [dict(title=row[0], description=row[1]) for row in DATA]

print "\nlist comp:\n{}\n".format(posts_list_comp)

# for loop

posts_dict = {}
posts = []

for item in DATA:
    posts_dict['title'] = item[0]
    posts_dict['description'] = item[1]
    posts.append(posts_dict)
    posts_dict = {}

print "\nfor loop:\n{}\n".format(posts)
