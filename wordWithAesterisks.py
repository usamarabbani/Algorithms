def censor(text,word):

    word_list = text.split()
   # result =''
    stars='*' *len(word)

  #  count =0

    index=0;
    for i in word_list:
        if i==word:
            word_list[index]=stars
        index+=1
    result=' '.join(word_list)
    return result



print(censor('i am very handsome, i can do very anything', 'very'))