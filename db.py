from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# my association table
association_table = db.Table('association', db.Model.metadata,  # groupchat and users
    db.Column('groupchat_id', db.Integer, db.ForeignKey('groupchat.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    )

# my classes
class Groupchat(db.Model):
    __tablename__ = 'groupchat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    messages = db.relationship('Message', cascade = 'delete')
    users = db.relationship('User', secondary=association_table, back_populates='user_groupchats')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'messages': [s.serialize() for s in self.messages],
            'users': [c.serialize() for c in self.users]
        }

    def limited_serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String, nullable=False)
    groupchat_id = db.Column(db.Integer,db.ForeignKey('groupchat.id'), nullable=False)
    groupchat_name = db.Column(db.String, nullable=False)


    def __init__(self,**kwargs):
        self.text = kwargs.get('text', '')
        self.sender_id = kwargs.get('sender_id')
        self.groupchat_id = kwargs.get('groupchat_id')
        self.groupchat_name = kwargs.get('groupchat_name')

    def serialize(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'text': self.text,
            'groupchat': {
                "id": self.groupchat_id,
                "name": self.groupchat_name
            }
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    user_groupchats = db.relationship('Groupchat', secondary=association_table, back_populates='users')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'groupchats': [c.limited_serialize() for c in self.user_groupchats]
        }
