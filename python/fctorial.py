def calc_fact(n):
    fact = 1
    for i in range(1, n+1 ,2):
        fact*=i
        print(fact)
calc_fact(6)