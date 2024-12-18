digits_16 = "0123456789ABCDEF"
def convert_to_base(n, base):
    # Базовый случай: если число меньше основания, возвращаем его как строку
    if n < base:
        return digits_16[n]
    else:
        # Рекурсивный вызов для перевода оставшейся части числа
        return convert_to_base(n // base,base) + digits_16[n % base]
# Запрос числа и основания у пользователя
user_input_number = int(input("Введите число для перевода: "))
user_input_base = int(input("Введите основание системы счисления: "))

# Проверка, чтобы основание было больше 1
if user_input_base <= 1:
    print("Основание системы счисления должно быть больше 1.")
else:
    # Вывод результата
    result = convert_to_base(user_input_number, user_input_base)
    print("Число", user_input_number," в системе счисления с основанием ",user_input_base," равно ",result)
