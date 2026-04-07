import json

# Создание файла example.json и сохранение в него словаря из Python в формате json
# если файл был уже - перезапишет, если нет - создаст
# data = {'user': 'user',
#         'role': 'admin'}
#
# with open('example.json', 'w') as file:
#     json.dump(data, file)
#
# with open('example.json') as file:
#     data_1 = json.load(file)
#
# print(data)

# user = {
#     "name": "Alex",
#     "age": 25,
#     "role": "QA"
# }
#
# with open('user.json', 'w') as file:
#     json.dump(user, file)
#
# user_upd = {
#     "name": "Alex",
#     "age": 25,
#     "role": "QA",
#     "skills": ["python", "testing"]
# }
#
# with open('user.json', 'w') as file:
#     json.dump(user_upd, file)
#
# with open('user.json', 'r') as file:
#     data = json.load(file)
#
# print(f'{data["name"]} works as {data["role"]}')
# for skill in data["skills"]:
#     print(skill)
#
# def check_age(json_data):
#     return json_data['age'] > 18
#
# def check_role(json_data):
#     return json_data['role'] == 'QA'
#
# def check_skill(json_data, skill):
#     return skill in json_data['skills']

# def get_name(json_data):
#     return json_data.get('name', 'No name')

users = [
    {"name": "Alex", "role": "QA"},
    {"name": "Ivan", "role": "dev"},
    {"name": "Anna", "role": "QA"}
]

with open('users.json', 'w') as file:
    json.dump(users, file)

with open('users.json') as file:
    json_data = json.load(file)

def qa_users(json_data):
    result = []
    for user in json_data:
        if user["role"] == "QA":
            result.append(user)
    return result

print(qa_users(json_data))