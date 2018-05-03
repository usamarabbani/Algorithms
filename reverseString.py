s="Hel  l o   "

def reverse(s):
    revstring=''
    index=len(s)
    while index>0:
        revstring+=s[index-1]
        index=index-1
    return revstring

print(reverse(s))

