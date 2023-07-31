user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key,value in user_0.items():
    print(f"\nkey:{key}")
    print(f"Value:{value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_languages.keys():
    print(f"{name.title()}")

print("====================\n")

for name_1 in favorite_languages:
    print(f"{name_1.title()}")