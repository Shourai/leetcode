class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}

        for ch in s:
            if ch not in counter:
                counter[ch] = 1
            else:
                counter[ch] += 1
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        res = ""
        for tuple in sorted_counter:
            res += (tuple[1] * tuple[0])

        return res


def case_one():
    input = "tree"
    output = "eetr"
    assert (Solution().frequencySort(input)) == output


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
