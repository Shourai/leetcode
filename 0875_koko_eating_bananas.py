from math import ceil

class Solution:
    def check(self, speed, piles, h):
        total = 0
        for pile in piles:
            total += ceil(pile/speed)
        print(total)
        return total <= h


    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_pile = 1
        max_pile = max(piles)

        while min_pile < max_pile:
            mid = (min_pile + max_pile) // 2
            if self.check(mid, piles, h):
                max_pile = mid
            else:
                min_pile = mid + 1

        return min_pile
            

def case_one():
    piles = [3, 6, 7, 11]
    h = 8
    output = 4
    assert (Solution().minEatingSpeed(piles, h)) == output


def case_two():
    piles = [30,11,23,4,20]
    h = 5
    output = 30
    assert (Solution().minEatingSpeed(piles, h)) == output


def case_three():
    piles = [30,11,23,4,20]
    h = 6
    output = 23
    assert (Solution().minEatingSpeed(piles, h)) == output


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
