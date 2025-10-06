def find_triplet_product(target_sum):
    for a in range(1, target_sum // 3):
        # Derive b from a and the target sum
        numerator = target_sum * (target_sum - 2 * a)
        denominator = 2 * (target_sum - a)
        
        # Check if b is a positive integer
        if numerator % denominator == 0:
            b = numerator // denominator
            
            # Since we iterate a in ascending order, if b > a, we check for the triplet
            if b > a:
                c = target_sum - a - b
                
                # Check the Pythagorean condition: a^2 + b^2 = c^2
                if a * a + b * b == c * c:
                    return a * b * c
    return 0

print(find_triplet_product(1000))