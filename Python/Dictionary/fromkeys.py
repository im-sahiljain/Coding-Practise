people: list[str] = ['Max', 'Alex', 'Hannah']
users: dict = dict.fromkeys(people)
print(users)

users: dict = dict.fromkeys(people ,'Unknown')
print(users)