
# def mail_checker_1(mail_to, mail_from, mail_text):
#     print('Получатель: {mail_to}')
#     print('Отправитель: {mail_from}')
#     print('Текст письма: {mail_text}')
#
# mail_box = {}
#
# def mail_checker_2(mail_to, mail_from, mail_text):
#     mail_box.setdefault(mail_to, []).append({mail_from:mail_text})
#
# # полученные письма
# mail_checker_2(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')
#
# mail_checker_2(mail_to='john_connor@yandex.ru', mail_from='sarah_connor@yandex.ru', mail_text='Сынок, надень шапку')
#
# mail_checker_2(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Правая рука чешется, не знаю, что и делать')
#
# mail_checker_2(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Что бы сказал на это твой отец?')
#
# print(mail_box)

# spam = []
# mail_box = {}
#
# def text_with_stop_words_check(text):
#     stop_words = ['Без вложений', 'Скидки', 'Распродажа', 'Выгода', 'Гарантия']
#     for w in stop_words:
#         if w in text:
#             return True
#     return False
#
# def is_spam(mail_text):
#     if mail_text == mail_text.isupper() or 'https' in mail_text or text_with_stop_words_check(mail_text):
#         return True
#     return None
#
#
# def mail_checker_3(mail_to, mail_from, mail_text):
#     if not is_spam(mail_text):
#         mail_box.setdefault(mail_to, []).append({mail_from: mail_text})
#         return
#     spam.append({mail_from: mail_text})



# Мое решение
# def sum_numbers(nums):
#     sum_nums = 0
#     for num in nums:
#         sum_nums += num
#     return sum_nums
#

# Улучшенный вариант
# def sum_numbers(nums):
#     return sum(nums)

# nums = [1, 2, 3, 4, 5]
#
# print(sum_numbers(nums))

#Мое решение
# def even_nums(nums):
#     even_nums_list = []
#     for num in nums:
#         if num % 2 == 0:
#             even_nums_list.append(num)
#     return even_nums_list
#

# Улучшение
# def even_nums(nums):
#     return [num for num in nums if num % 2 == 0]
# nums = [1, 2, 3, 4, 5, 6]
#
# print(even_nums(nums))
#


#def count_symbols(text):
#     result = {}
#
#     for i in text:
#         result.setdefault(i, 0)
#         result[i] += 1
#     return result
#

# Улушчение
# def is_the_element(list_of_elements):
#     return 'admin' in list_of_elements
# text = "qa automation"
#


# def is_the_element(list_of_elements):
#     if 'admin' in list_of_elements:
#         return True
#     else:
#         return False

# Мое решение
def list_unique(elements_1, elements_2):
    result = []
    for i in elements_1:
        if i not in result:
            result.append(i)
        else:
            continue

    for i in elements_2:
        if i not in result:
            result.append(i)
        else:
            continue
    return result

# Улучшение _1
def list_unique(elements_1, elements_2):
    result = []

    for i in elements_1 + elements_2:
        if i not in result:
            result.append(i)

    return result

# Улучшение максимально короткий код
def list_unique(elements_1, elements_2):
    return list(set(elements_1 + elements_2))

a = [1, 2, 3]
b = [3, 4, 5]
print(list_unique(a,b))




