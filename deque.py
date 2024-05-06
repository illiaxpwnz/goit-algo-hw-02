from collections import deque
import re

def is_palindrome(s):
    # Підготовка рядка: видалення небуквених символів, перетворення в нижній регістр
    s = re.sub(r"[^a-z0-9]", "", s.lower())

    # Створення deque з символів рядка
    d = deque(s)

    # Перевірка на паліндром за допомогою видалення та порівняння символів з обох кінців
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Тестування функції
test_strings = ["A man a plan a canal Panama", "Hello", "Able was I saw Elba"]
for string in test_strings:
    print(f"'{string}' is a palindrome: {is_palindrome(string)}")
