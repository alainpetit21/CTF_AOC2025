from engine.Challenge import Challenge


class ChallengeDay1C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)

        self.result = 0



    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)


    def run(self):
        pos_start = 50
        cpt_zero = 0

        for row in self.data:
            direction = row[0]
            nbStep = int(row[1:])


            for i in range(nbStep):
                if direction == 'L':
                    pos_start -= 1
                elif direction == 'R':
                    pos_start += 1
                else:
                    assert False

                pos_start %= 100

                if pos_start == 0:
                    cpt_zero += 1

        self.result = cpt_zero
        return self.result
