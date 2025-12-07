from engine.Challenge import Challenge


class ChallengeDay4C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.h = 0
        self.w = 0

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)
        self.w = len(self.data[0])
        self.h = len(self.data)

    def get_at(self, x, y):
        if x < 0 or y < 0:
            return '.'

        if x >= self.w or y >= self.h:
            return '.'

        return self.data[y][x]

    def run(self):
        roll_assessed = 0

        for y, row in enumerate(self.data):
            for x, c in enumerate(row):
                if c == '.':
                    continue

                cpt_in_kernel = 0
                for kernel_x in [-1, 0, 1]:
                    for kernel_y in [-1, 0, 1]:
                        c2 = self.get_at(kernel_x + x, kernel_y + y)
                        if kernel_y == 0 and kernel_x == 0:
                            continue

                        if c2 == '.':
                            continue

                        cpt_in_kernel += 1

                if cpt_in_kernel < 4:
                    print(f"{y}:{x}:{cpt_in_kernel}")
                    roll_assessed += 1


        self.result = roll_assessed
        return self.result
