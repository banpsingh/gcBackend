import json
from flask import Flask, request
from db import db
import dao


app = Flask(__name__)
db_filename = "gc.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

# my routes
@app.route('/')
@app.route('/api/groupchats/') # gets all groupchats
def get_all_groupchats():
    return success_response(dao.get_all_groupchats())

@app.route('/api/groupchats/', methods=['POST']) # create new gc
def create_groupchat():
    body = json.loads(request.data)
    groupchat = dao.create_groupchat(
        name = body.get('name')
    )
    return success_response(groupchat, 201)

@app.route('/api/groupchats/<int:groupchat_id>/') # get gc by id
def get_groupchat_by_id(groupchat_id):
    groupchat = dao.get_groupchat_by_id(groupchat_id)
    if groupchat is None:
        return failure_response("Groupchat not found!")
    return success_response(groupchat)

@app.route('/api/groupchats/<int:groupchat_id>/', methods=['DELETE']) # delete gc by id
def delete_groupchat(groupchat_id):
    groupchat = dao.delete_groupchat_by_id(groupchat_id)
    if groupchat is None:
        return failure_response("Groupchat not found!")
    return success_response(groupchat)

@app.route('/api/users/') # get all users
def get_all_users():
    return success_response(dao.get_all_users())

@app.route('/api/users/<int:user_id>/') #get user by id
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/api/users/', methods=['POST']) # create new user
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        name = body.get('name')
    )
    return success_response(user, 201)

@app.route('/api/users/<int:user_id>/', methods=['DELETE']) # delete user by id
def delete_user(user_id):
    user = dao.delete_user_by_id(user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/api/groupchats/<int:groupchat_id>/add/', methods=['POST']) # add user to gc by gc_id
def add_user_to_groupchat(groupchat_id):
    body = json.loads(request.data)
    groupchat = dao.add_user_to_groupchat(
        groupchat_id,
        body.get('user_id'),
    )
    if groupchat is None:
        return failure_response("Groupchat not found!")
    return success_response(groupchat)


@app.route('/api/groupchats/<int:groupchat_id>/message/', methods=['POST']) # create new message by gc_id
def create_message(groupchat_id):
    groupchat = get_groupchat_by_id(groupchat_id)
    if groupchat is None:
        return failure_response("Groupchat not found!")
    body = json.loads(request.data)
    message = dao.create_message(
        groupchat_id,
        body.get('sender_id'),
        body.get('text')
    )
    if message == -1:
        return failure_response('Sender does not exist')
    elif message == 1:
        return failure_response('Sender is not in this groupchat')
    return success_response(message)

@app.route('/api/groupchats/<int:groupchat_id>/message/<int:message_id>/', methods=["POST"])# update message
def update_message(groupchat_id,message_id):
    groupchat = get_groupchat_by_id(groupchat_id)
    if groupchat is None:
        return failure_response("Groupchat not found!")
    body = json.loads(request.data)
    new_message = dao.update_message(
        message_id,
        body.get('sender_id'),
        body.get('text')
    )
    if new_message == -1:
        return failure_response("Sender does not exist!")
    elif new_message == 1:
        return failure_response("Message does not exist!")
    elif new_message == 0:
        return failure_response("The sender is not the owner of this message")
    return success_response(new_message)






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
