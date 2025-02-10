class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers:
            return sum(map(int, numbers.replace("\n", ",").split(",")))
        return 0