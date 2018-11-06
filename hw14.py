import requests

url = "https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text"

r = requests.get(url)

r.encoding = 'utf8'

data = str(r.text)


p0=0

 

wordList=[]

 

while data.find('<p id',p0) != -1:

 

    p1=data.find('<p id',p0)

 

    p2=data.find('>',p1+1)

 

    p3=data.find('</p>',p2)

 

    temp=data[p2+1:p3]

 

    p4=temp.find('<')

 

    while p4 != -1:

 

        p5=temp.find('>',p4)

 

        temp = temp[:p4]+temp[p5+1:]

 

        p4=temp.find('<')

 

    p0=p3+1

 

    #print(temp)

 

    words=temp.split()

 

    #print(words)

 

    for word in words :

 

        word=word.replace('.','')

 

        word=word.replace(',','')

 

        word=word.replace('"','')

 

        word=word.replace('“','')

 

        word=word.replace('”','')

 

        word=word.replace(':','')

 

        

 

        word=word.replace('’s','')

 

        wordList.append(word)

mydict={}

for w in wordList:

    if w in mydict:

        mydict[w] += 1

    else:

        mydict[w] = 1

#print(mydict)

 

count=0

for k in sorted(mydict, key=mydict.__getitem__, reverse=True):

    print('%s: %s'%(k, mydict[k]))

    count+=1

    if count >= 20:

        break
