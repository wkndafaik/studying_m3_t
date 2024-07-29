# main.py

from op import add, sub, mul, div
print('Здравствуйте!')


def main():
    print('Калькулятор')
    print('Нажмите Z, чтобы выйти')

    while True:
        op = input('Варианты действий: +, -, *, /: ')
        if op == 'Z':
            print('До свидания...')
            break

        if op not in ['+', '-', '*', '/']:
            print('Неправильная операция, попробуйте снова.')
            continue

        try:
            n1 = float(input('Введите первое число: '))
            print(f'Первое число: {n1}')
            n2 = float(input('Введите второе число: '))
            print(f'Второе число: {n2}')
        except ValueError:
            print('Введите, пожалуйста, именно числа.')
            continue

        try:
            res = 0
            if op == '+':
                res = add(n1, n2)
            elif op == '-':
                res = sub(n1, n2)
            elif op == '*':
                res = mul(n1, n2)
            elif op == '/':
                res = div(n1, n2)

            print(f'Результат:  {res}')
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
