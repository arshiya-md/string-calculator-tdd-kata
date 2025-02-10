class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers:
            if numbers.startswith("//"):
                delimiter = numbers[2:3]
                numbers = numbers[4:]
                return sum(map(int, numbers.replace("\n", ",").split(delimiter)))
            return sum(map(int, numbers.replace("\n", ",").split(",")))
        return 0