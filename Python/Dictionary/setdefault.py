users: dict = {0:'Max', 1:'Alex', 2:'Hannah'}
print(users.setdefault(0,'???'))
print(users.setdefault(99,'???'))
print(users)