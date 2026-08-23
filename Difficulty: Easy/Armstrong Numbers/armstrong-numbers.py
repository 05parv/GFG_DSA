class Solution:
    def armstrongNumber(self, n):
        total = 0
        num = n

        nod = len(str(n))

        while num > 0:
            last_digit = num % 10
            total += last_digit ** nod
            num = num // 10

        return total == n