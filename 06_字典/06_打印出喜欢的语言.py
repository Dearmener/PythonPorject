favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil','sarah']

for name in favorite_languages.keys():
    if name in friends:
        print(f"{name.title()} like {favorite_languages[name].title()}")

for firend in friends:
    print(f"{firend.title()}")