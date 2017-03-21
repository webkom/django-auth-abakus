success_login_webkom = {
    'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6IndlYmtvbUBhYm'
             'FrdXMubm8iLCJ1c2VybmFtZSI6IndlYmtvbSIsImV4cCI6MTQ4NTk4MjAzMSwib3JpZ19pYXQiOjE0O'
             'DUzNzcyMzF9.ejw6M-0wfXoJ3PnHju0nRxmwgeJkUZJhhFUPqRTs1Q8',
    'user': {
        'id': 1,
        'username': 'webkom',
        'firstName': 'webkom',
        'lastName': 'webkom',
        'fullName': 'webkom webkom',
        'email': 'webkom@abakus.no',
        'picture': 'http://127.0.0.1:10000/RW0ZuNdP8djH2fczlbxFzpID9TM=/400x400/abakus.png',
        'isStaff': True,
        'isActive': True,
        'abakusGroups': [
            {'id': 1, 'name': 'Users'},
            {'id': 2, 'name': 'Abakus'},
            {'id': 11, 'name': 'Webkom'}
        ],
        'isAbakusMember': True,
        'isAbakomMember': True,
        'penalties': [],
        'icalToken': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    }
}
success_login_bedkom = {
    "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6ImJlZGtvbUBhYm'
             'FrdXMubm8iLCJ1c2VybmFtZSI6ImJlZGtvbSIsImV4cCI6MTQ4OTg3OTI3Mywib3JpZ19pYXQiOjE0O'
             'DkyNzQ0NzN9.Lc-uqgLZJHoEr9kbDhTOX8oxJL7vPDs-Lp8O9aEVNnY',
    "user": {
        "id": 2,
        "username": "bedkom",
        "firstName": "bedkom",
        "lastName": "bedkom",
        "fullName": "bedkom bedkom",
        "email": "bedkom@abakus.no",
        "profilePicture":
            "http://127.0.0.1:10000/xSa2q902k-WENWxFgaI00sJKIzw=/200x200/default_female_avatar.png",
        "gender": "",
        "allergies": "",
        "isStaff": False,
        "isActive": True,
        "abakusGroups": [
            {
                "id": 1,
                "name": "Users"
            },
            {
                "id": 2,
                "name": "Abakus"
            },
            {
                "id": 6,
                "name": "Bedkom"
            }
        ],
        "isAbakusMember": True,
        "isAbakomMember": True,
        "penalties": [],
        "icalToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
}

success_login_pleb = {
    "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6ImJlZGtvbUBhYm'
             'FrdXMubm8iLCJ1c2VybmFtZSI6ImJlZGtvbSIsImV4cCI6MTQ4OTg3OTI3Mywib3JpZ19pYXQiOjE0O'
             'DkyNzQ0NzN9.Lc-uqgLZJHoEr9kbDhTOX8oxJL7vPDs-Lp8O9aEVNnY',
    "user": {
        "id": 100,
        "username": "pleb",
        "firstName": "pleb",
        "lastName": "pleb",
        "fullName": "pleb pleb",
        "email": "pleb@stud.ntnu.no",
        "profilePicture":
            "http://127.0.0.1:10000/xSa2q902k-WENWxFgaI00sJKIzw=/200x200/default_female_avatar.png",
        "gender": "",
        "allergies": "",
        "isStaff": False,
        "isActive": True,
        "abakusGroups": [
            {
                "id": 1,
                "name": "Users"
            },
            {
                "id": 2,
                "name": "Abakus"
            }
        ],
        "isAbakusMember": True,
        "isAbakomMember": False,
        "penalties": [],
        "icalToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
}

invalid_login = {
    "nonFieldErrors": [
        "Unable to login with provided credentials."
    ]
}

success_login_alumni_not_member = {
    "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJlbWFpbCI6ImJlZGtvbUBhYm'
             'FrdXMubm8iLCJ1c2VybmFtZSI6ImJlZGtvbSIsImV4cCI6MTQ4OTg3OTI3Mywib3JpZ19pYXQiOjE0O'
             'DkyNzQ0NzN9.Lc-uqgLZJHoEr9kbDhTOX8oxJL7vPDs-Lp8O9aEVNnY',
    "user": {
        "id": 100,
        "username": "alumni",
        "firstName": "alumni",
        "lastName": "alumni",
        "fullName": "alumni alumni",
        "email": "alumni@alumni.no",
        "profilePicture":
            "http://127.0.0.1:10000/xSa2q902k-WENWxFgaI00sJKIzw=/200x200/default_female_avatar.png",
        "gender": "",
        "allergies": "",
        "isStaff": False,
        "isActive": True,
        "abakusGroups": [
            {
                "id": 1,
                "name": "Users"
            }
        ],
        "isAbakusMember": False,
        "isAbakomMember": False,
        "penalties": [],
        "icalToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
}

invalid_login = {
    "nonFieldErrors": [
        "Unable to login with provided credentials."
    ]
}
