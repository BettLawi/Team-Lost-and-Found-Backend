from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Define a one-to-many relationship between Users and Lostitem
    lost_items = relationship("LostItem", back_populates="user")

    # Define a one-to-one relationship between Users and FoundItem
    found_item = relationship("FoundItem", back_populates="user", uselist=False)

    # Define a one-to-one relationship between Users and Itemsreturnedtoowner
    items_returned = relationship("ItemsReturnedToOwner", back_populates="user", uselist=False)

    # Define a one-to-many relationship between Users and Reward
    rewards = relationship("Reward", back_populates="user")

    # Define a one-to-many relationship between Users and Comment
    comments = relationship("Comment", back_populates="user")

    def __repr__(self):
        return f'(id={self.id}, name={self.username} email={self.email})'

class LostItem(db.Model):
    __tablename__ = 'lostitems'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String)
    item_description = db.Column(db.String)
    image_url = db.Column(db.String)
    reported_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Define a one-to-one relationship between LostItem and Reward
    reward = relationship("Reward", back_populates="lost_item", uselist=False)

    # Define a many-to-one relationship between LostItem and Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("Users", back_populates="lost_items")

class Reward(db.Model):
    __tablename__ = 'rewards'

    id = db.Column(db.Integer, primary_key=True)
    reward_amount = db.Column(db.String)
    item_name = db.Column(db.String)

    # Define a many-to-one relationship between Reward and Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("Users", back_populates="rewards")

    # Define a one-to-one relationship between Reward and LostItem
    item_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    lost_item = relationship("LostItem", back_populates="reward", uselist=False)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    lostitem_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))

    # Define a many-to-one relationship between Comment and Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("Users", back_populates="comments")

class FoundItem(db.Model):
    __tablename__ = 'founditems'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    item_name = db.Column(db.String)
    reward_id = db.Column(db.Integer)
    image_url = db.Column(db.String)

    # Define a one-to-one relationship between FoundItem and Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship("Users", back_populates="found_item", uselist=False)

class ItemsReturnedToOwner(db.Model):
    __tablename__ = 'itemsreturnedtoowner'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('lostitems.id'))
    datereturned = db.Column(db.DateTime, server_default=db.func.now())

    # Define a one-to-one relationship between ItemsReturnedToOwner and Users
    user = relationship("Users", back_populates="items_returned", uselist=False)
