# 添加一个小河流
river = {
    'changjiang': 'China',
    'Ocean': "USA",
    'Nile': 'Egypt'
}

for key in river:
    print(f"The {key} runs trough {river.get(key)}")

for k,v in river.items():
    print(f"The {k} runs trough {v}")

for key in river:
    print(f"{key.title()}")

for value in river:
    print(f"{value.title()}")
