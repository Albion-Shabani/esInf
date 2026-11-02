def clamp(lista : list[float], limite:float ):
    for i in range(len(lista)):
        if lista[i] > limite:
            lista[i] = limite

l = [2,3,5,1,4]
clamp(l,3)
print(l)