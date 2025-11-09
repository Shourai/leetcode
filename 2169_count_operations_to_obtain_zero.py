class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
                count += 1
            else:
                num2 -= num1
                count += 1
            print(num1, num2)
        return count


def case_one():
    num1 = 2
    num2 = 3
    print(Solution().countOperations(num1, num2))


def case_two():
    num1 = 10
    num2 = 10
    print(Solution().countOperations(num1, num2))


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
