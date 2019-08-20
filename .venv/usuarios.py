
users = [
    {
        'id': 1,
        'nome': 'Gabriel'
    }, {
        'id': 2,
        'nome': 'João'
    }, {
        'id': 3,
        'nome': 'Paulo'
    }, {
        'id': 4,
        'nome': 'Pedro'
    }
]

#lista todoos usuarios
def all_users():
    return users

def remove_user(id):

    users[id - 1] = {
        "id": id,
        "status": "DELETED"
    }
    return True

#adicioan usario

def append(data):
    users.append(data)