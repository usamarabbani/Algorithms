"""
Anagram:
Given two strings, check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, only the order 
of characters can be different. For example, “act” and “tac” are anagram of each other.
"""
import string
str_1 = "practice makes perfect"
str_2 = "perfect makes practice"

str_3 = "allergy"
str_4 = "allergic"


def is_anagram(str_1, str_2):
    str_1 = str_1.replace(" ","")
    str_2 = str_2.replace(" ", "")

    if len(str_1) !=len(str_2):
        return False

    str_1=str_1.lower()
    str_2=str_2.lower()

    #alphabet="abcdefghijklmnopqurstuvwxyz"

    dic_1=dict.fromkeys(list(string.ascii_lowercase),0)
    dic_2 = dict.fromkeys(list(string.ascii_lowercase),0)

    for i in range(len(str_1)):
        dic_1[str_1[i]]+=1
        dic_2[str_2[i]]+=1
    return dic_1==dic_2


# Is an anagram:
print(is_anagram(str_1, str_2))

# Is not an anagram:
print(is_anagram(str_3,str_4))