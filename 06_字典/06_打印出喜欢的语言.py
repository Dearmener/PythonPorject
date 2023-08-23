favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    if name in friends:
        print(f"{name.title()} like {favorite_languages[name].title()}")

for var in favorite_languages.values():
    print(f"{var.title()}")
print("=============================")
for name in favorite_languages.keys():
    print(f"{name.title()}")
print("===========================")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}")

print("====通过set进行去重===")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")
