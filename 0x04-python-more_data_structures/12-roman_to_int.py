#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return (0)

    roman_dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    numb = 0

    for i in range(len(roman_string)):
        if roman_dic.get(roman_string[i], 0) == 0:
            return (0)

        current = roman_dic[roman_string[i]]
        next = roman_dic[roman_string[i + 1]]

        if (i != (len(roman_string) - 1) and (current < next)):
                numb += roman_dic[roman_string[i]] * -1
        else:
            numb += roman_dic[roman_string[i]]

    return numb
