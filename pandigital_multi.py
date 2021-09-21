#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def find_pand():
    digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(9000, 10000):
        test =  str(i*1)+str(i*2)
        if set(test).difference(set(digits))==[]:
            return test

print(find_pand())
