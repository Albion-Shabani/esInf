def rec_common_suffix(str1,str2):
    if str1 == "" or str2 == "" or str1[-1] != str2[-1]:
        return 0
    return 1 + rec_common_suffix(str1[:-1], str2[:-1])


print(rec_common_suffix("ciao", "ciao"))