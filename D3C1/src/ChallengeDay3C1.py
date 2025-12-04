from engine.Challenge import Challenge


class ChallengeDay3C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

    def find_highest(self, number) -> tuple[int, int]:
        #print(number)
        highest = 0
        highest_pos = -1

        for i, c in enumerate(number):
            n = int(c)
            if n > highest:
                highest = n
                highest_pos = i


        return highest, highest_pos


    def run(self):
        highests = []

        for row in self.data:
            value1, pos1 = self.find_highest(row[0:-1])
            value2, pos2 = self.find_highest(row[:pos1:-1])

            highests.append(int(str(value1) + str(value2)))

        self.result = sum(highests)
        return self.result
