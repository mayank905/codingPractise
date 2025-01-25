import math
# print(math.log2(2))
# print(math.log2(4))
# print(math.log2(8))
# print(math.log2(15))
# print(math.log2(30))

# Function to convert decimal number
# to binary using recursion
# def DecimalToBinary(num):
    
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')

# # Driver Code
# if __name__ == '__main__':
    
#     # decimal value
#     dec_val = 24
    
#     # Calling function
#     DecimalToBinary(dec_val)

# prime number storing sieve
'''
sieve = [1] * (max_element + 1)
        sieve[1] = 0
        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            if sieve[i] == 1:
                for j in range(i * i, max_element + 1, i):
                    sieve[j] = 0

#method 2
def bitwiseSieve(srt, n):

    prime = [0 if i % 2 == 0 else 1 for i in range(n+1)]
    prime[1] = 0
    prime[2] = 1

    i = 3
    while (i * i <= n):
        if (prime[(i)] == 1):
            j = i * i
            while (j <= n):
                prime[j] = 0
                j += 2*i
        i += 2
    i = srt
    result=[]
    while (i <= n):
        if (prime[i] == 1):
            result.append(i)
        i += 1
    return result
'''

def dec2bin1(number: int):
    ans = ""
    if ( number == 0 ):
        return 0
    while ( number ):
        ans += str(number&1)
        number = number >> 1
    
    ans = ans[::-1]

    return ans 

def dec2bin2(number):
    ans=""
    for i in range(31, -1, -1):
        k = number >> i
        ans+=str(k & 1)
    return ans


def main():
    number = 61
    number1=10**9
    print(number1.bit_count())
    print(f"The binary of the number {number} is {dec2bin1(number)}")
    print(f"The binary of the number {number} is {dec2bin2(number)}")


# driver code
if __name__ == "__main__":
    main()

