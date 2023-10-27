from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationship with Lostitem (Reported by)
    lostitems_reported = relationship('Lostitem', back_populates='user_reported')

class Lostitem(db.Model):
    __tablename__ = 'lostitems'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    item_description = db.Column(db.String)
    image_url = db.Column(db.String)
    isfound = db.Column(db.Boolean)
    isreturnedtoowner = db.Column(db.Boolean)
    reported_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationship with User (User who reported)
    user_reported_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_reported = relationship('User', back_populates='lostitems_reported')

    # Relationship with Reward (Has Reward)
    reward = relationship('Reward', uselist=False, back_populates='lostitem')

    # Relationship with Comment (Comment on)
    comments = relationship('Comment', back_populates='lostitem')

class Reward(db.Model):
    __tablename__ = 'rewards'

    id = db.Column(db.Integer, primary_key=True)
    rewardamount = db.Column(db.String)

    # Relationship with Lostitem (Has Reward)
    lostitem_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    lostitem = relationship('Lostitem', back_populates='reward')

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    
    # Relationship with Lostitem (Comment on)
    lostitem_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    lostitem = relationship('Lostitem', back_populates='comments')
