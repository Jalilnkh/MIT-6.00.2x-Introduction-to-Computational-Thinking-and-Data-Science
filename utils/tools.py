def fibo_simple(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fibo_simple(number - 1) + fibo_simple(number - 2)

def fibo_memo(number, memo={}):
    if number == 0 or number == 1:
        return 1
    try:
        return memo[number]
    except:
        result = fibo_memo(number - 1, memo) + fibo_memo(number - 2, memo)
        memo[number] = result
        return memo[number]    