#Secret code language 

# if the word contains atleast 3 charachters, remove the first letter and append it at the end , 
#now append 3 random charachters at the starting and the end .
#else 
#simple reverse the string

#decoding

#if the word contains lesss than 3 charachters, reverse it else:

#remove the first 3 charachters from the start and end and then remove the last charachter and append it at the start of the word.



st=input('enter the word:')
words=st.split(" ")
operation=input("press 1 for coding and 0 for decoding :")
if(operation=="1"):
    nwords=[]
    for word in words:
        if (len(word)>=3):
            r1="abc"
            r2="xyz"
            st_new= r1+word[1:]+word[0]+r2
            nwords.append(st_new)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if (len(word)>=3):
            st_new=word[3:-3]
            st_new=st_new[-1]+st_new[:-1]
            nwords.append(st_new)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

