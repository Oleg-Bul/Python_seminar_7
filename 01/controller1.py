import game1
import game2
import view
import logger
import random


def run():
    i = 0
    while i < 3:
        mode = view.choose_mode()
        if mode == 'Крестики нолики':
            print("Игра №", i)
#            result = game1.run_game()
            result = random.randint(0, 2)
            view.show_results(result)
            logger.log_result(i, result)
        if mode == 'Конфеты':
            print("Игра №", i)
#            result = game2.run_game()
            result = random.randint(0, 2)
            view.show_results(result)
            logger.log_result(i, result)
        i += 1
