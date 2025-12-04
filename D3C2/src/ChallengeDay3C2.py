from engine.Challenge import Challenge


class ChallengeDay3C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)


    def find_highest(self, number, lenght) -> str:
        if lenght == 0:
            return ''

        #print(number)
        highest = 0
        highest_pos = -1

        for i in range(0, len(number) - lenght + 1):
            n = int(number[i])
            if n > highest:
                highest = n
                highest_pos = i

        next_highest = self.find_highest(number[highest_pos+1:], lenght - 1)

        return str(highest) + next_highest


    def run(self):
        highests = []

        for i, row in enumerate(self.data):
            print(f"Running row {i} of {len(self.data)}")

            highest = self.find_highest(row, 12)
            highests.append(int(highest))

        self.result = sum(highests)
        return self.result
