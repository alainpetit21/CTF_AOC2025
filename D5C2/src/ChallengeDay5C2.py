from math import trunc
from typing import List

from D5C2.src.Range import Range
from engine.Challenge import Challenge



class ChallengeDay5C2(Challenge):
    def __init__(self, filename=None):
        super().__init__(filename)
        self.result = 0
        self.fresh_ranges: List[Range] = []

    def detect_fix_overlap(self):
        found_overlap = True

        while found_overlap:
            found_overlap = False

            for i, range1 in enumerate(self.fresh_ranges):
                for j, other_range in enumerate(self.fresh_ranges):
                    if i == j:
                        continue

                    print(f"Checking range {i}...with range {j}")
                    if range1.is_overlap(other_range):
                        found_overlap = True
                        range1.merge(other_range)
                        self.fresh_ranges.remove(other_range)
                        break

                if found_overlap:
                    break



    def interpret_data(self, data_inj: List[str] = None):
        super().interpret_data(self.data)

        for row in self.data:
            #if there is a '-' .. this is a range
            if '-' in row:
                fresh_range = Range(tuple([int(r) for r in row.split('-')]))
                self.fresh_ranges.append(fresh_range)
            elif '' == row:
                print("Found the separator")
            else:
                ...

        self.detect_fix_overlap()

    def run(self):
        cpt_ingredients = 0

        for i, fresh_range in enumerate(self.fresh_ranges):
            # print(f"Processing {i} of {len(self.fresh_ranges)}")

            cpt_ingredients+= fresh_range.end - fresh_range.start + 1

        self.result = cpt_ingredients
        return self.result
