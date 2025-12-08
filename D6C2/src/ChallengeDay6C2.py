from typing import List

from engine.Challenge import Challenge



class ChallengeDay6C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.operations = []
        self.operators = []

    def load_data(self, name_input: str = None) -> List[str]:
        with open(name_input, "r") as file:
            self.data = [r for r in file.readlines()]
            return self.data

    def interpret_data(self, data_inj: List[str] = None):
        data = self.data
        nb_digits = len(data) - 1
        len_x = len(data[0])
        operands = []

        #Read octopus math for nombers
        for i in range(len_x):
            operand = ""

            for j in range(nb_digits):
                operand += data[j][len_x-i-2]

            try:
                operand = int(operand)
                operands.append(operand)
            except ValueError:
                self.operations.append(operands)
                operands = []

        #Read operations
        self.operators = data[nb_digits].strip().split()
        self.operators.reverse()

    def do_operation(self, operand1, operand2, operator):
        result = 0
        if operator == '+':
            result = operand1 + operand2
        elif operator == '*':
            result = operand1 * operand2

        return result

    def run(self):
        results = []

        for i, operation in enumerate(self.operations):

            result = operation[0]
            for j in range(1, len(operation)):
                result = self.do_operation(result, operation[j], self.operators[i])

            results.append(result)

        self.result = sum(results)
        return self.result
