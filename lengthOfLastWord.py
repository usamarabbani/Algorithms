def lenthOFLastWord(self,s):
    s=s.strip()


    num=0
    for i in reversed(range(len(s))):
        if s[i]==' ':
            break
            num +=1
    return num