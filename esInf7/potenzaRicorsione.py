def recursive_pow(base, potenza):
    if potenza == 0:
        return 1
    return base * recursive_pow(base,potenza-1)

print(recursive_pow(2,0))