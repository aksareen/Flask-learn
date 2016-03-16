from app import db
from models import BlogPost

#create the databasae and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Good","I\'m Good."))
db.session.add(BlogPost("Well","I\'m Well."))


#commit the changes
db.session.commit()
