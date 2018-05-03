#cracking the code questions
#1.1
'''string= "abcevff"

def isUniqueChars(str):

    if len(str)>128:
        return False

    arr= [False] *128

    for char in str:
        if arr[ord(char)] is False:
            arr[ord(char)] = True
        else:
            return False
    return True

print (isUniqueChars(string))'''


def isUniqueChars2(string):
    unchar=[]
    for c in string:
        for c in unchar:
            return False
    else:
        unchar.append(c)
    return True

print(isUniqueChars2(string="jjajjsjjdhhdfkkksaaa"))



'''def is_Unique(s):
    return len(s)== len(set(s))

s1= "#@!#$%^&#dfvdhdsksie945959"
s2= "pokeman"

print(is_Unique(s1))
print(is_Unique(s2))'''


