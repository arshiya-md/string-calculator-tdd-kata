import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        # If custom delimiters are provided, extract and process them
        if numbers.startswith("//"):
            delimiter_part, numbers = numbers.split("\n", 1)
            delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
            if not delimiters:
                delimiters = [delimiter_part[2:]]  # Extract the single delimiter
            for delim in delimiters:
                numbers = numbers.replace(delim, ",")
        else:
            # Use a comma to split numbers when no custom delimiters are given
            numbers = numbers.replace("\n", ",")
            
        numbers_list = list(map(int, numbers.split(',')))
        
        negatives = []
        numbers_upto_1000 = []
        
        for num in numbers_list:
            if num < 0:
                negatives.append(num)
            elif num <= 1000:
                numbers_upto_1000.append(num)

        if negatives:
            raise ValueError(f"Negative numbers not allowed {', '.join(map(str, negatives))}")

        return sum(numbers_upto_1000)