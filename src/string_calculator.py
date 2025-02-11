import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiters = ['\n', ',']
        
        if numbers.startswith("//"):
            delimiter_part, numbers = numbers.split('\n',1)
            delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
            
        for delim in delimiters:
            numbers = numbers.replace(delim, ",")
            
        splitted_numbers = list(map(int, numbers.split(',')))
        negatives = [num for num in splitted_numbers if num < 0]
        numbers_upto_1000 = [num for num in splitted_numbers if num <= 1000]
        
        if negatives:
            raise ValueError(f"Negative numbers not allowed {', '.join(map(str, negatives))}")
        
        return sum(numbers_upto_1000)