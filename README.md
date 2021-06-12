# AppDev Final Project SP2020: Group Chat Backend

This app is a group chat messaging app. You can make group chats and users can join multiple group chats and send messages to the chat.
The public server IP address for this app is: http://35.190.171.142/

# Expected Functionality
## Get all group chats
```
GET /api/groupchats/
```
```javascript
Response

{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "rubber emulsifyeet",
            "messages": [<SERIALIZED MESSAGE>],
            "users": [<SERIALIZED USERS WITHOUT GROUP CHAT USERS>]
        },
        ...
    ]
}
```
## Make new group chat
```
POST /api/groupchats/
```
```javascriipt
Request

{
    "name": <USER INPUT>
}
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "messages": [],
        "users": []
    }
}
```
## Get a specific group chat
```
GET /api/groupchats/{id}/
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "messages": [<SERIALIZED MESSAGES>],
        "users": [<SERIALIZED USERS WITHOUT GROUP CHAT USERS>]
    }
}
```
## Delete a specific group chat
```
DELETE /api/groupchats/{id}/
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "messages": [<SERIALIZED MESSAGES>],
        "users": [<SERIALIZED USERS WITHOUT GROUP CHAT USERS>]
    }
}
```
## Get all users
```
GET /api/users/
```
```javascript
Response

{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "bob",
            "groupchats": [<SERIALIZED GROUP CHATS THAT BOB IS IN>]
        },
        ...
    ]
}
```
## Create new user
```
POST /api/users/
```
```javascriipt
Request

{
    "name": <USER INPUT>
}
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID> ,
        "name": <USER INPUT FOR NAME>,
        "groupchats": []
    }
}
```
## Get a specific user
```
GET /api/users/{id}/
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "groupchats": [<SERIALIZED GROUP CHATS THIS USER IS IN>]
    }
}
```
## Delete a specific user
```
DELETE /api/users/{id}/
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "groupchats": [<SERIALIZED GROUP CHATS THIS USER IS IN>]
    }
}
```
## Add user to a group chat
```
POST /api/groupchats/{ID}/add/
```
```javascript
Request

{
	"user_id": <USER INPUT>
}
```
```javascript
Response

{
    "success": true,
    "data": <SERIALIZED GROUP CHAT>    
}
```
## Send message to group chat
```
POST /api/groupchats/{ID}/message/
```
```javascript
Request

{
	"sender_id": <USER INPUT>,
	"text": <USER INPUT>
}
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "sender_id": <SENDER_ID USER INPUT>,
        "text": "beep",
        "groupchat": {
            "id": 1,
            "name": "rubber emulsifyeet"
        }
    }
}
```
## Editing an existing message
```
POST /api/groupchats/{gID}/message/{mID}/
```
```javascript
Request

{
	"sender_id": <USER INPUT>,
	"text": <USER INPUT FOR UPDATED MESSAGE>
}
```
```javascript
Response

{
    "success": true,
    "data": {
        "id": <ID>,
        "sender_id": <SENDER_ID USER INPUT>,
        "text": <UPDATED MESSAGE TEXT INPUT>,
        "groupchat": {
            "id": 1,
            "name": "rubber emulsifyeet"
        }
    }
}
```
