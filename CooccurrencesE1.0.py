import sys,string,re
dic={}
words=re.findall(r"\w+",open(sys.argv[1], mode='r', encoding='utf-8').read().lower()) #pull all words in the text file in the 1st arrgument and put them in words variable
for i in range(len(words)-int(sys.argv[2])+1): #for each word in the list of words does the next :
    coc=words[i:i+int(sys.argv[2])] #remplis coc par n mots a la fois fill coc with n element (from the second argument)
    if len(coc[0])==int(sys.argv[4]) and len(coc[-1])==int(sys.argv[5]): dic[str(coc)]=dic.get(str(coc),0)+1 #push coc if the first word length is = (4th argument) and the length of the last word is = (5th argument)
for i in dic.keys(): 
    if dic.get(i) == int(sys.argv[3]): print( i , dic.get(i)) #print all cooccurrences in dic with m frequancy (3rd argument)
 