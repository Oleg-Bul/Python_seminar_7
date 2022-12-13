# Сборка общего решения

import game1
import game2
import View
import Logger
def run():
    mode = View.choose_mode():
    if mode == 'Крестики нолики':
        result = game1.run_game()
        View.show_results(result)
        Logger.log_result(result)
    if mode == 'Конфеты':
        result = game2.run_game()
        View.show_results(result)
        Logger.log_result(result)