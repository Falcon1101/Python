file= '/Users/vagishmishra/Desktop/python/India External Offer .txt'
#file= input('Enter the file name with path: ')
try:
    fhand = open(file,"r")
except:
    print('File name or path is not correct: ',file)
    quit()
count=-1
case= input('Do you want your search case sensitive Y/N: ')
dictionary = dict()
fullread = fhand.read()
n_words  = fullread.split()
if case=='Y':
    words  = n_words
else:
    words=[z_words.lower() for z_words in n_words]
wlist = list()
while True:
    i=input('Enter word or write "O D" to get result: ')
    if i=='O D':
        break
    else:
        wlist.append(i)

for word in words:
    dictionary[word]=dictionary.get(word,0)+1
while count<len(wlist)-1:
    count=count+1
    try:
        print (wlist[count],dictionary[wlist[count]])
    except:
        print(wlist[count],'not in the file')
        continue
