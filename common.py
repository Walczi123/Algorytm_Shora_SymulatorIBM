def run_function(function, number, *args):
    z = None
    n = number
    ans = []
    while 1:
        print(f"function {str(function.__name__)}({n}) starts")
        z = function(n, *args)
        ans.append(z)
        if z is None or z == 1:
            break
        n = n//z
        if n == 1:
            break
    return ans
