def fact(n):
    if n == 0:
        return 1
    else:
        summ = 1
        for i in range (1, n+1):
            summ *= i
        return summ

def step(n, ro):
    return ((ro ** n) / fact(n))

def pi_zero (n, m, ro):
    result = 0
    for i in range (n+1):
        result += ((ro ** i) / fact(i))
    second= ((ro**(n+1)) / (n*fact(n))) * ((1-((ro/n)**m)) / (1-(ro/n)))
    result += second
    return result ** -1

def pi_otk (n, m, ro):
    return ((ro**(n+m)/(n**m*fact(n))) * pi_zero(n, m, ro))


def main():
    lambda_day = 4
    mu = 2.08
    m = 4
    n = 4



    ro = round(lambda_day/mu, 3)
    print ("pi_otk = ", pi_otk(n, m, ro))
    t_obs = 1/mu

if __name__ == "__main__":
    main()