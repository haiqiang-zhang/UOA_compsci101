def prime_factorization(n):
    whether_prime = True
    list_result = []
    if n ==1:
        whether_prime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                whether_prime = False
                break
    while whether_prime == False:
        for j in range(2, n):
            whether_prime_j = True
            if j == 1:
                whether_prime_j = False
            else:
                for i in range(2, j):
                    if j % i == 0:
                        whether_prime_j = False
                        break
            if whether_prime_j == True and n % j == 0:
                n = n // j
                list_result.append(j)
                break
        whether_prime = True
        if n == 1:
            whether_prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    whether_prime = False
                    break
    list_result.append(n)
    return list_result

def print_prime_list(a_list):
    for i in range(len(a_list)):
        if i != len(a_list) - 1:
            print(a_list[i],end = " * ")
        else:
            print(a_list[i])


n = 2
prime_list = prime_factorization(n)
print(n, "is the product of the following primes:", end=" ")
print_prime_list(prime_list)
n = 21
prime_list = prime_factorization(n)
print(n,"is the product of the following primes:",end=" ")
print_prime_list(prime_list)
n = 56
prime_list = prime_factorization(n)
print(n,"is the product of the following primes:",end=" ")
print_prime_list(prime_list)