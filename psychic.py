from random import randint

class Psychic():
    def __init__(self, count):
        self._count   = count
        self._history = []
        self._history_answers = []
        self._numbers = [0 for _ in range(count)]
        self._trust   = [0 for _ in range(count)]

    def generate_numbers(self):
        self._numbers = [randint(5, 49) * 2 + (1 - i%2) for i in range(self._count)]

        if len(self._history_answers) < len(self._history):
            self._history_answers.append('')

        self._history.append(self._numbers)

    def check_answer(self, number):
        self._history_answers.append(number)

        for i in range(self._count):
            if self._numbers[i] == number:
                self._trust[i] += 5
                if self._trust[i] > 100:
                    self._trust[i] = 100
            else:
                self._trust[i] -= 5
                if self._trust[i] < 0:
                    self._trust[i] = 0

    def get_trusts(self):
        return self._trust

    def get_numbers(self):
        return self._numbers

    def get_history(self):
        return (self._history, self._history_answers)

    def get_count(self):
        return self._count

