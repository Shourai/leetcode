class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        arr = []
        for i in range(len(words)):
            if x in words[i]:
                arr.append(i)
        return arr


def case_one():
    words = ["leet", "code"]
    x = "e"
    print(Solution().findWordsContaining(words, x))


def case_two():
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "a"
    print(Solution().findWordsContaining(words, x))


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
