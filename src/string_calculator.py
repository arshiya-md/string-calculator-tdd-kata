class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers:
            return sum(map(int, numbers.split(",")))
        return 0