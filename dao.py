from db import db, Groupchat, Message, User

# GROUPCHAT
def get_all_groupchats():
    return [t.serialize() for t in Groupchat.query.all()]

def create_groupchat(name):
    new_groupchat = Groupchat(
        name= name
    )

    db.session.add(new_groupchat)
    db.session.commit()
    return new_groupchat.serialize()


def get_groupchat_by_id(groupchat_id):
    groupchat = Groupchat.query.filter_by(id=groupchat_id).first()
    if groupchat is None:
        return None
    return groupchat.serialize()

def delete_groupchat_by_id(groupchat_id):
    groupchat = Groupchat.query.filter_by(id=groupchat_id).first()
    if groupchat is None:
        return None

    db.session.delete(groupchat)
    db.session.commit()
    return groupchat.serialize()

# USER
def get_all_users():
    return [t.serialize() for t in User.query.all()]

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

def create_user(name):
    new_user = User(
        name=name
    )

    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()

def delete_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None

    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def add_user_to_groupchat(groupchat_id, user_id):
    groupchat = Groupchat.query.filter_by(id=groupchat_id).first()
    if groupchat is None:
        return None
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    groupchat.users.append(user)
    db.session.commit()
    return groupchat.serialize()

# MESSAGE
def create_message(groupchat_id, sender_id, text):
    groupchat= Groupchat.query.filter_by(id=groupchat_id).first()
    if groupchat is None:
        return None
    groupchat_name = groupchat.name
    user = User.query.filter_by(id=sender_id).first()
    if user is None:
        return -1 # the sender does not exist
    if user not in groupchat.users:
        return 1 # the sender i not in the groupchat
    new_message = Message(
        text= text,
        sender_id=sender_id,
        groupchat_id=groupchat_id,
        groupchat_name=groupchat_name
    )

    db.session.add(new_message)
    db.session.commit()
    return new_message.serialize()

def update_message(message_id, sender_id, text):
    user = User.query.filter_by(id=sender_id).first()
    if user is None:
        return -1 # user doesnt exist

    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return 1 # message doesnt exist
    if message.sender_id != sender_id:
        return 0 # user is not the sender of this message

    message.text = text

    db.session.commit()
    return message.serialize()
