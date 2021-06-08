class Solution:
    def repeatedNumber(self, A):
        """ Return the value of repeated number and missing number in the given array
        using the standard formulaes of Sum of n Natural numbers and sum of squares of n Natural Numbers"""
        array = []
        array = A
        sum_of_num = 0
        sum_of_squares = 0
        for num in array:
            sum_of_num += num
            sum_of_squares += num*num
            # pass
        x = len(array)
        sum_of_num_expected = (x * (x+1)) / 2
        sum_of_squares_expected = ((x) * (x+1) * (2*x+1)) / 6

        # Assuming A is present twice and B is missing:
        # B - A
        b_minus_a = sum_of_num_expected - sum_of_num
        # B^2 - A^2 = (B-A) * (B+A)
        b2_minus_a2 = sum_of_squares_expected - sum_of_squares
        # B + A
        b_plus_a = b2_minus_a2 / b_minus_a

        a = (b_plus_a - b_minus_a) / 2
        b = (b_plus_a + b_minus_a) / 2
        return int(a), int(b)



arr = [1,2,3,4,5,7,7]
print(Solution().repeatedNumber(arr))
