class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        if numbers.startswith("//"):
            delimiter = numbers[2:3]
            numbers = numbers[4:]
        else:
            delimiter = ","
        splitted_numbers = list(map(int, numbers.replace("\n", ",").split(delimiter)))
        negatives = [num for num in splitted_numbers if num < 0]
        numbers_upto_1000 = [num for num in splitted_numbers if num <= 1000]
        
        if negatives:
            raise ValueError(f"Negative numbers not allowed {', '.join(map(str, negatives))}")
        
        return sum(numbers_upto_1000)