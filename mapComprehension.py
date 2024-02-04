users = [
    ("bob",32,"bobPass"),
    ("rob",32,"robPass"),
    ("eob",32,"eobPass"),
    ("mob",32,"mobPass")
]

userNameMapping = {user[0] : user for user in users}

print(userNameMapping)
print(userNameMapping["rob"])