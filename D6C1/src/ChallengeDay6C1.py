from typing import List

from engine.Challenge import Challenge



class ChallengeDay6C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.operands = []
        self.operators = []

    def interpret_data(self, data_inj: List[str] = None):
        super().interpret_data(self.data)

        for row in self.data:
            try:
                operands = [int(o) for o in row.split()]
                self.operands.append(operands)
            except ValueError:
                operators =  [o for o in row.split()]
                self.operators.append(operators)

    def do_operation(self, operand1, operand2, operator):
        result = 0
        if operator == '+':
            result = operand1 + operand2
        elif operator == '*':
            result = operand1 * operand2

        return result

    def run(self):
        results = []

        for i in range(len(self.operands[0])):
            nb_operands = len(self.operands)

            result = self.operands[0][i]
            for j in range(1, nb_operands):
                result = self.do_operation(result, self.operands[j][i], self.operators[0][i])

            results.append(result)

        self.result = sum(results)
        return self.result
