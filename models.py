# models.py

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(255))
    Lastname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phonenumber = db.Column(db.Integer)
    role = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP)
    lost_items = db.relationship('LostItem', backref='user', lazy=True)
    rewards = db.relationship('Reward', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    found_items = db.relationship('FoundItem', backref='user', lazy=True)
    items_returned = db.relationship('ItemReturnedToOwner', backref='user', lazy=True)

class LostItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255))
    description = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_url = db.Column(db.String(255))
    reward_id = db.Column(db.Integer, db.ForeignKey('reward.id'))
    reported_at = db.Column(db.TIMESTAMP)

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward_amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('lost_item.id'), nullable=False)
    item_name = db.Column(db.String(255))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lost_id = db.Column(db.Integer, db.ForeignKey('lost_item.id'), nullable=False)

class FoundItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('lost_item.id'), nullable=False)
    item_name = db.Column(db.String(255))
    reward_id = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

class ItemReturnedToOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('lost_item.id'), nullable=False)
    datereturned = db.Column(db.TIMESTAMP)
