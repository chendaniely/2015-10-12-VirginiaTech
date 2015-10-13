def f_k(temperature):
    return((temperature - 32) * (5 / 9.0) + 273.15)

def k_c(temp):
    return(temp - 273.15)

def f_c(temp):
    temp_k = f_k(temp)
    result = k_c(temp_k)
    return(result)

assert f_k(212) == 373.15
assert f_k(32) == 273.15
