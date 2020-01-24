class Situation:
    def __init__(self, str_input, str_output, int_i, int_point):
        self.input = str_input
        self.output = str_output
        self.index = int_i
        self.point = int_point

    def __eq__(self, other):
        return (self.output == other.output and self.input == other.input
                and self.point == other.point and self.index == other.index)

    def __hash__(self):
        return hash((self.output, self.input, self.point, self.index))
