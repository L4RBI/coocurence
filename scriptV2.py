import sys,string,re
dic={}
words=re.findall(r"\w+",open(sys.argv[1], mode='r', encoding='utf-8').read().lower()) # remplis words par tous les mots se trouvant dans text-b
for i in range(len(words)-int(sys.argv[2])+1): #boucle de i=0 --> la taille de la list 
    coc=words[i:i+int(sys.argv[2])] #remplis coc par n mots a la fois
    if len(coc[0])==int(sys.argv[4]) and len(coc[-1])==int(sys.argv[5]): dic[str(coc)]=dic.get(str(coc),0)+1 #remplis le dict en verifiant les conditions de taille du 1er et dernnier mots et incremente leur frequence
for i in dic.keys(): 
    if dic.get(i) == int(sys.argv[3]): print( i , dic.get(i)) #affiche les mots qui verfie la condition de frequence
 