def BigMinus(s1, s2):
    num_1 = int(s1)
    num_2 = int(s2)
    result = num_1 - num_2
    return str(result) if result >0 else str(-result)