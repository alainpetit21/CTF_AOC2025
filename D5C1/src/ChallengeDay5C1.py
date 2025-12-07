from math import trunc

from engine.Challenge import Challenge


class ChallengeDay5C1(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.fresh_ranges = []
        self.ingredients = []

    def interpret_data(self, data_inj: [str] = None):
        super().interpret_data(self.data)

        for row in self.data:
            #if there is a '-' .. this is a range
            if '-' in row:
                self.fresh_ranges.append(tuple([int(r) for r in row.split('-')]))
            elif '' == row:
                print("Found the separator")
            else:
                self.ingredients.append(row)


    def run(self):
        freshes = set()

        for ingredient in self.ingredients:
            n = int(ingredient)

            for fresh_range in self.fresh_ranges:
                if fresh_range[0] <= n <= fresh_range[1]:
                    print(f"Ah! this is fresh: {ingredient} range: {fresh_range}")
                    freshes.add(ingredient)

        self.result = len(freshes)
        return self.result
