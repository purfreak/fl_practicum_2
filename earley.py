from situation import Situation


class Earley:
    rules_list = []
    situations_dict = dict()

    def __init__(self, word):
        situation = Situation('U', 'S', 0, 0)
        self.situations_dict = {i: set() for i in range(len(word) + 1)}
        self.situations_dict[0].add(situation)
        self.word = word

    def add_rule(self, rule):
        self.rules_list.append(rule)

    def add_situation(self, situation, list_number):
        self.situations_dict[list_number].add(situation)

    def scan(self, list_number, symbol):
        for situation in self.situations_dict[list_number]:
            if situation.output[situation.point] == symbol:
                sit = Situation(situation.input, situation.output, situation.index, situation.point + 1)
                self.add_situation(sit, list_number + 1)

    def predict(self, list_number):
        situations_to_insert = []
        for situation in self.situations_dict[list_number]:
            if situation.point < len(situation.output):
                nonterminal = situation.output[situation.point]
                for rule in self.rules_list:
                    if rule.input == nonterminal:
                        sit = Situation(nonterminal, rule.output, list_number, 0)
                        situations_to_insert.append(sit)

        for situation in situations_to_insert:
            self.add_situation(situation, list_number)

    def complete(self, list_number):
        situations_to_insert = []
        for situation in self.situations_dict[list_number]:
            list_number_2 = situation.index
            if situation.point == len(situation.output):
                for situation_2 in self.situations_dict[list_number_2]:
                    sit = Situation(situation_2.input, situation_2.output, situation_2.index, situation_2.point + 1)
                    situations_to_insert.append(sit)

        for situation in situations_to_insert:
            self.add_situation(situation, list_number)

    def get_answer(self):
        prev_len = len(self.situations_dict[0])
        self.predict(0)
        self.complete(0)
        new_len = len(self.situations_dict[0])

        while new_len != prev_len:
            prev_len = new_len
            self.predict(0)
            self.complete(0)
            new_len = len(self.situations_dict[0])

        for i in range(1, len(self.word) + 1):
            self.scan(i - 1, self.word[i - 1])
            prev_len = len(self.situations_dict[i])
            self.predict(i)
            self.complete(i)
            new_len = len(self.situations_dict[i])

            while new_len != prev_len:
                prev_len = new_len
                self.predict(i)
                self.complete(i)
                new_len = len(self.situations_dict[i])

        for situation in self.situations_dict[len(self.word)]:
            if situation.input == 'U' and situation.output == 'S' and situation.index == 0 and situation.point == 1:
                return True

        return False
