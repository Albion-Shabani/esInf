def len_common_prefix(str1,str2):
    if len(str1) >= len(str2):
        min = str2
    else:
        min = str1
    
    count = 0

    for i in range(len(min)):
        if str1[i] == str2[i]:
            count += 1

    return count


print(len_common_prefix("carta", "carota"))

    
