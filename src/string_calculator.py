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
        
        for num in splitted_numbers:
            if num < 0:
                raise ValueError(f"Negative numbers not allowed {num}")
        
        return sum(splitted_numbers)