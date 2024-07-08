from gameparts import Board
# Из файла exception.py, который лежит в gameparts,
# импортируем класс FieldIndexError
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(string):
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(f'{string}')
    file.close


def main():
    game = Board()
    current_player = 'X'
    game.display()
    # первым ходят крестики
    # Это флаговая переменная. ПО умолчанию игра запущена и продолжается.
    running = True
    game.display()

    # тут запускается основной цикл игры.
    while running:
        print(f'Ход делает {current_player}')
        # Запускается бесконечный цикл
        while True:
            # в этом блоке содержатся операции, которые могут
            # вызвать исключения.
            try:
                row = int(input('Введите номер строки: '))
        # Если введеное значение меньше нуля или больше иди равно
        # field_size (это значение равно трём, оно хранится в модуле
        # parts.py)...
                if row < 0 or row >= game.field_size:
                    # ... выбросить исключение FieldIndexError
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    # ... выбросить исключение FieldIndexError
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise ConnectionError(
                        'Ячейка занята.'
                        ' Введите другие координаты.'
                    )
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print(
                    'Пожалуйста, введите значение'
                    ' для строки и столбца заново.'
                )
                continue
            except ValueError:
                # ...выводятся сообщения...
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значение'
                      ' для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите значения для строки и столбца заново.')
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break
        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            string = f'Победили {current_player}\n'
            save_result(string)
            print(f'Победили {current_player}')
            running = False
        elif game.is_board_full():   
            print('Ничья')
            string = 'Ничья\n'
            save_result(string)
            running = False
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
