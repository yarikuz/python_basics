"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""



x = 5
y = "Барборис"
z = 2.78
print(x)
print(y, z)

x, y, z = "Аркадий", "Константин", "Евгений"
print(x)
print(y)
print(z)

somebody = input("Введите что-нибудь:")
somebodyelse = input("Введите что-нибудь еще:")
print(f"Вот, что вы ввели: {somebody}, Кроме того: {somebodyelse}")
