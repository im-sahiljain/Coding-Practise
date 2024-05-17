users: dict = {0:'Max', 1:'Alex', 2:'Hannah'}
print(users.get(1))
print(users.get(999))
print(users.get(999,'Missing'))