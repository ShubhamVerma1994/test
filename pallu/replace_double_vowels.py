def replace_double_vowels(str_1):
    str_new = ""
    for i in range(0, len(str_1)-1):
        if str_1[i] == str_1[i + 1] and str_1[i].lower() in "aeiou":
            continue
        else:
            str_new += str_1[i]
    return str_new


res = replace_double_vowels("school")
print(res)
