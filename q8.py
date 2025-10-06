def find_greatest_product(number_string, length):
    greatest_product = 0
    
    for i in range(len(number_string) - length + 1):
        substring = number_string[i:i + length]
        current_product = 1
        
        for digit_char in substring:
            current_product *= int(digit_char)
            
        if current_product > greatest_product:
            greatest_product = current_product
            
    return greatest_product

