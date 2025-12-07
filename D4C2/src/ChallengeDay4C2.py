from typing import Tuple, List

from engine.Challenge import Challenge


class ChallengeDay4C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)

        self.result = 0
        self.h = 0
        self.w = 0

    def interpret_data(self, data_inj: List[str] = None):
        super().interpret_data(self.data)

        self.data = [[c for c in r] for r in self.data]
        self.w = len(self.data[0])
        self.h = len(self.data)

    def get_at(self, x, y):
        if x < 0 or y < 0:
            return '.'

        if x >= self.w or y >= self.h:
            return '.'

        return self.data[y][x]

    def run(self):
        roll_assessed = 9999
        cpt_removed = 0

        while roll_assessed > 0:
            print(f"Just removed {roll_assessed} last iteration")
            list_assessed:List[Tuple[int, int]] = []

            for y, row in enumerate(self.data):
                for x, c in enumerate(row):
                    if c == '.' or c == 'x':
                        continue

                    cpt_in_kernel = 0
                    for kernel_x in [-1, 0, 1]:
                        for kernel_y in [-1, 0, 1]:
                            c2 = self.get_at(kernel_x + x, kernel_y + y)
                            if kernel_y == 0 and kernel_x == 0:
                                continue

                            if c2 == '.' or c2 == 'x':
                                continue

                            cpt_in_kernel += 1

                    if cpt_in_kernel < 4:
                        list_assessed.append((x, y))

            roll_assessed = len(list_assessed)

            #Remove the assessed
            for assessed in list_assessed:
                self.data[assessed[1]][assessed[0]] = 'x'
                cpt_removed+= 1

        self.result = cpt_removed
        return self.result
