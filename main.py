# 1
def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "отлично",
        "B": "очень хорошо",
        "C": "хорошо",
        "D": "удовлетворительно",
        "E": "достаточно",
        "FX": "неудовлетворительно",
        "F": "неудовлетворительно",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    if option == "description":
        return get_description
    return None


# 2
DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    global DEFAULT_DISCOUNT
    for k, v in customer.items():
        if k == "discount":
            return price * (1 - v)
    return price * (1 - DEFAULT_DISCOUNT)


# 3


def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n):
        if n in cache:
            result = cache[n]
        else:
            result = cache.get(n - 1, fibonacci(n - 1)) + cache.get(n - 2, fibonacci(n - 2))
            cache[n] = result
        return result

    return fibonacci


# 4


def discount_price(discount):
    def price(price):
        return price * (1 - discount)

    return price


# 5

def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        if len(result) == 10 and result.startswith("0"):
            new_phone1 = "+38" + result
            return new_phone1
        if len(result) == 12 and result.startswith('38'):
            new_phone2 = "+" + result
            return new_phone2

    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


# 6

import re


def generator_numbers(string=""):
    number = re.findall("\d+", string)
    for i in number:
        yield int(i)


def sum_profit(string):
    sum = 0
    for i in generator_numbers(string):
        sum += i
    return sum

# 7


def normal_name(list_name):
    return list(map(str.title, list_name))


# 8


def get_emails(list_contacts):
    return list(map(lambda x: x.get("email"), list_contacts))


list_contacts = [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False}]


# 9


def positive_values(list_payment):
    return list(filter(lambda x: x > 0, list_payment))

# 10


def get_favorites(contacts):
    return list(filter(lambda x: x.get("favorite"), contacts))


# 11

from functools import reduce


def sum_numbers(numbers):
    return reduce((lambda x,y: x+y), numbers)


# 12


def amount_payment(payment):
    return reduce(lambda x, y: x+y, filter(lambda x: x > 0, payment), 0)


print(amount_payment([-1, 3, 4]))



