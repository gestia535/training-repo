# 1. Sum in the list

# def sum_in_list(num_list):
#     return sum(num_list)
#
# nums = [1, 2, 3, 4, 5]
# print(sum_in_list(nums))

# 2. Even nums filter

# def even_nums_filter(num_list):
#     even_list = [i for i in num_list if i % 2 == 0]
#     return even_list
#
# nums = [1, 2, 3, 4, 5, 6]
# print(even_nums_filter(nums))

# 3. Max num

# def max_num(num_list):
#     max_number = num_list[0] #сохраняем первое значение в списке, чтобы было с чем сравнивать
#     for i in num_list:
#         if i > max_number:
#             max_number = i
#     return max_number
#
# nums = [-10, -3, -2, -15]
# print(max_num(nums))

# 4. Count symbols

# def count_symbols(string_new):
#     result_dict = {}
#     for l in string_new:
#         result_dict.setdefault(l, 0)
#         result_dict[l] += 1
#     return result_dict
#
# text = ""
# print(count_symbols(text))

# 5. Check presence

# def is_admin_present(list_roles):
#     return "admin" in list_roles

# users = ["test", "qa"]
# print(is_admin_present(users))

# 6. Unify lists without duplication

# def unify_no_duplicates(list_1, list_2):
#     new_list = list_1 + list_2
#     result_list = []
#     for i in new_list:
#         if i not in result_list:
#             result_list.append(i)
#     return result_list
#
# a = [1, 2, 3]
# b = [3, 4, 5]
#
# print(unify_no_duplicates(a,b))

# 7. Users description
# user = {
#         "name": "Ivan",
#         "age": 25,
#         "role": "QA"
#     }
#
# def description_user(user):
#     description = f"{user['name']} is {user['age']} years old and works as {user['role']}"
#     return description
#
# print(description_user())

# 8. Dictionary filter

# users = {
#     "user1": 18,
#     "user2": 25,
#     "user3": 16
# }
#
# def dictionary_filter(dictionary):
#     new_dict = {}
#     for key, value in dictionary.items():
#         if value > 18:
#             new_dict[key] = value
#     return new_dict
#
# print(dictionary_filter(users))

# 9. Count words in text

# def count_words(text_str):
#     result_dict = {}
#     new_list = text_str.split()
#     for word in new_list:
#         result_dict.setdefault(word, 0)
#         result_dict[word] += 1
#     return result_dict
#
# text = "qa qa automation test qa"
# print(count_words(text))

# 10. Login validation
# users = ["admin", "qa_user", "test123"]
#
# def login_validation(login):
#     if login in users:
#         return('OK')
#     else:
#         return('NOT FOUND')
#
# login_validation('kshf')