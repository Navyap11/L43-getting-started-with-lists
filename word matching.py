def wordsmatch(wrds):
    counter= 0
    list=[]
    for word in wrds:
        if len(word)>1 and word[0]==word[-1]:
            counter +=1
            list.append(word)
    
    print("The words that have the same value in the last and first place list: \n",list)
    return counter

count=wordsmatch(["cde", "cdc", "hei", "heh", "naan", "1234321"])
print("The amount of values taht have the first and last cgarecter same is: ",count)