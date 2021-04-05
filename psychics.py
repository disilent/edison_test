from random import randint

class Psychic():
    def __init__(self):
        self._history = []
        self._number  = 0
        self._trust   = 0

    def generate_number(self):
        self._number = randint(10, 99)
        self._history.append(self._number)

    def check_answer(self, number):
        if self._number == number:
            self._trust += 5
            if self._trust > 100:
                self._trust = 100
        else:
            self._trust -= 5
            if self._trust < 0:
                self._trust = 0

    def get_trust(self):
        return self._trust

    def get_number(self):
        return self._number

    def get_history(self):
        return self._history


class PsychicsIterator():
    def __init__(self, psychics):
        self._psychics = psychics
        self._index = 0

    def __next__(self):
        if self._index < len(self._psychics):
            self._index += 1
            return self._psychics[self._index - 1]

        raise StopIteration


class Psychics():
    def __init__(self, count):
        self._count    = count
        self._psychics = [Psychic() for _ in range(count)]
        self._answers  = []

        self._number_count = 0

    def generate_numbers(self):
        if len(self._answers) < self._number_count:
            self._answers.append('')

        for psychic in self._psychics:
            psychic.generate_number()

        self._number_count += 1

    def check_answer(self, number):
        self._answers.append(number)

        for psychic in self._psychics:
            psychic.check_answer(number)

    def get_trusts(self):
        return [psychic.get_trust() for psychic in self._psychics]

    def get_numbers(self):
        return [psychic.get_number() for psychic in self._psychics]

    def get_history(self):
        return (list(zip(*(psychic.get_history() for psychic in self._psychics))), self._answers)

    def __len__(self):
        return self._count

    def __getitem__(self, key):
        return self._psychics[key]

    def __iter__(self):
        return PsychicsIterator(self)

    def get_count(self):
        return self.__len__()

    def get_psychic(self, key):
        return self.__getitem__(key)

