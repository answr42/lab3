import string

#Функция, проверяющая простое число
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return d * d > num

#Функция для нахождения НОД (наибольшего общего делителя), алгоритм Евклида
def NOD (k, t):
    while(k != t):
        if(k > t):
            k -= t
        else:
            t -= k
    return k

#Функция для нахождения открытой экспоненты
def find_e(fun):
    e = 0
    i = 2
    while (e == 0):
        if (NOD(i, fun) == 1 and e < fun):
            e = i
        else:
            i += 1
    return e

#Функция для нахождения закрытой экспоненты
def find_d (fun, e):
    d = 2
    br_wh = 1
    while(br_wh):
        if((d * e) % fun == 1):
            br_wh = 0
        else:
            d += 1
    return d

#Функция для шифрования сообщения
def code (list_symb_code, e, n):

    encoded_list = list()
    for b in list_symb_code:
        encoded_list.append((b**e) % n)

    return encoded_list

#Функция для расшифровки сообщения
def decode(encoded_list, d, n):
    decoded_list = list()
    for b in encoded_list:
        decoded_list.append((b**d) % n)
    return decoded_list

#Функция для ввода и проверки p и q
def vars():
    p = int(input("Введите p: "))
    q = int(input("Введите q: "))
    if not(is_prime(p) and is_prime(q)):
        print("Оба числа должны быть простыми")
        vars()
    elif p == q:
        print('Числа p и q не должны быть равны')
        vars()
    return p, q

#Функция для ввода и перевода в код сообщения
def msq_entr():
    s = input("Введите текст: ")

    list_symb = list()
    for b in s:
        list_symb.append(b)

    str_cp = s.encode('cp1251')
    list_symb_code = list()
    for b in str_cp:
        if (b > 223 and b < 256):
            list_symb_code.append(int(b - 223))
        else:
            msq_entr()

    return list_symb, list_symb_code

#Основная функция, где вызываются вспомогательные
def main ():
    # вводим данные
    p, q = vars()
    list_symb, list_symb_code = msq_entr()

    #вычисляем модуль n
    n = p * q

    #Вычисляем значение функции Эйлера
    fun = (p - 1) * (q - 1)

    #Выбираем открытую экспоненту
    e = find_e(fun)
    print("Открытый ключ: {%d,%d}"%(e, n))

    #Вычисляем закрытую экспоненту
    d = find_d(fun, e)
    print("Закрытый ключ: {%d,%d}"%(d, n))

    #Выводим данные
    print("Сообщение: ", list_symb)
    print("Код сообщения: ", list_symb_code)

    #Получаем зашифрованное сообщение
    encoded_list = code(list_symb_code, e, n)
    print("Зашифрованное сообщение: ", encoded_list)

    # Получаем расшифрованное сообщение
    decoded_list = decode(encoded_list, d, n)
    print("Шифрованное сообщение (после дешифрования): ", decoded_list)

    print("Конец программы. Хотите начать заново? (введите да или нет)")
    cont = input("")
    if(cont == "да"):
        print("\n")
        main()
    else:
        exit()

main()
