def prime_number_finder():
    def check_prime(n):
        if n < 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            return True
    def find_prime(lower, upper):
        prime = []
        for num in range(lower, upper +1):
            if check_prime(num):
                prime.append(num)
        return prime
    lower = int(input("enter your starting number: "))
    upper = int(input("enter your last number: "))
    primes = find_prime(lower, upper)
    print(f"Prime Number Between {lower} and {upper} is: \n", primes)
    ask = input("want to generate again ?(yes/no)").lower()
    if ask == "yes":
        prime_number_finder()
    else:
        print("Existing")
prime_number_finder()