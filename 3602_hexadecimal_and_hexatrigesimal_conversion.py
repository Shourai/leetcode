class Solution:
    def encode_base16(self, number):
        """Encode a number into Base36."""
        characters = "0123456789ABCDEF"
        result = ""

        while number > 0:
            number, remainder = divmod(number, 36)
            result = characters[remainder] + result

        return result or characters[0]  # Return '0' if the number is zero

    def encode_base36(self, number):
        """Encode a number into Base36."""
        characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        while number > 0:
            number, remainder = divmod(number, 16)
            result = characters[remainder] + result

        return result or characters[0]  # Return '0' if the number is zero

    def concatHex36(self, n: int) -> str:
        return self.encode_base16(n**2) + self.encode_base36(n**3)


def case_one():
    pass


def case_two():
    pass


def case_three():
    pass


if __name__ == "__main__":
    case_one()
    case_two()
    case_three()
