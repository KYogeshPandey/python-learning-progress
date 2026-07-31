# fetch names from a list of dict

users = [

    {
        'name':'rahul',
        'age' : 30,
        'gender': 'male'
    },

    {
        'name':'sohan',
        'age' : 30,
        'gender': 'male'
    },

    {
        'name':'geeta',
        'age' : 30,
        'gender': 'female'
    }
]

print(list(map(lambda users : users['gender',], users)))