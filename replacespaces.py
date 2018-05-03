# Write a method to replace all spaces in a string with '%20'.

def urlifyString(str):
    res = []
    #start = False
    str = str.strip()  # Removes white space from the beginning and end of the string
    for char in reversed(str):
        if (char == ' '):
            res += '02%'
        else:
            res += char
    res = ''.join(res[::-1])
    return res


print(urlifyString("       Mr John   Smith           "))

# O(n)