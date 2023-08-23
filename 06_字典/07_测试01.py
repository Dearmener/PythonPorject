favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

person_list = {'jen','sarah','edward','phil','meng','startker'}

for person in person_list:
    if person in favorite_languages:
        print(f"{person.title()},thank for your sub")
    else:
        print(f"{person.title()},take your time to particulate this surver")

print("================")

for p in favorite_languages.keys():
    if p in person_list:
        print(f"{p.title()},thank for your time")