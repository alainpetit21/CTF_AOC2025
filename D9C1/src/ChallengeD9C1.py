from typing import List

from engine.Challenge import Challenge
from itertools import permutations, combinations


def calculate_area(corner1, corner2):
    u = 0
    l = 0
    b = 0
    r = 0

    if corner1[0] <= corner2[0]:
        l = corner1[0]
        r = corner2[0]
    else:
        l = corner2[0]
        r = corner1[0]

    if corner1[1] <= corner2[1]:
        u = corner1[1]
        b = corner2[1]
    else:
        u = corner2[1]
        b = corner1[1]

    area = (r - l + 1) * (b - u + 1)
    print(corner1, corner2, area)

    return area



class ChallengeD9C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.red_tiles = []

    def interpret_data(self, data_inj: List[str] = None):
        super().interpret_data(self.data)

        for i, line in enumerate(self.data):
            #print(i)
            x, y = line.split(",")
            self.red_tiles.append((int(x), int(y)))
            # print(self.red_tiles)

    def run(self):
        comb = combinations(self.red_tiles, 2)

        biggest = 0
        for corners in comb:
            #print(corners)

            area = calculate_area(corners[0], corners[1])

            if area > biggest:
                biggest = area

        #print(biggest)

        self.result = biggest
        return self.result
