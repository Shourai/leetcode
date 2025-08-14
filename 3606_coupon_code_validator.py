import re
class Solution:
    def validateCoupons(
        self, code: list[str], businessLine: list[str], isActive: list[bool]
    ) -> list[str]:
        valid_coupons = []
        priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid_bussinesses = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i, j, k in zip(code, businessLine, isActive):
            if (
                i == ""
                or re.match(r'^[A-Za-z0-9_]+$', i)
                or j not in valid_bussinesses
                or k is not True
            ):
                continue
            else:
                valid_coupons.append((i, j))
        sorted_coupons = sorted(valid_coupons, key=lambda x: (priority[x[1]], x[0]))

        print([i for i, _ in sorted_coupons])
        return [i for i, _ in sorted_coupons]


def case_one():
    code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
    businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"]
    isActive = [True, True, True, True]

    solution = Solution()
    solution.validateCoupons(code, businessLine, isActive)


def case_two():
    code = [
        "pBXoMqBU0_aMgc9F8dy6TaSzza3KjSJFjxZa_NuyMjzEBR7fJNwpGHh7lzuoZvQeEUeo6YumHmIOjjchXlzSVa4ItdyDOImQgm",
        "P8rIIUl35MW8yrqRbO0N_IITptYOxz9tOCbPL6d1aIF_hM2sapaDtUzNpmAZRmJQB1WgjLh8bdYADuSRSU21OzttUkq73qiA66",
        "aFWkYookQlHYMXzhVGxbnrXIl1810ws3qHtketHSECHqJoktWXVZGc6ZyeOuzA_VL9zFL9znpIHwbkwJF2bOPQqsz3_0PYgETJ",
    ]
    businessLine = ["pharmacy", "invalid", "pharmacy"]
    isActive = [True, True, True]

    solution = Solution()
    solution.validateCoupons(code, businessLine, isActive)


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
