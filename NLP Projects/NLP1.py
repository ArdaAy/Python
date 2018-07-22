import codecs
import re
class NLP1:
    #reeding file with utf-8
    file = codecs.open("text.txt", "r", "utf-8")
    wordCount = 0
    wordLength = 0
    average = 0
    myList = []
    i = 0
    
    #adding every line of file to myList array
    for line in file:
        myList.insert(i, line.encode("utf-8"))
        i += 1
    
    for a in myList:
        r = codecs.decode(a, "utf-8")
        print(r)
        # print(a.decode('utf-8'))
        # match = re.findall(r'\S+l[ae]r.*\b', codecs.decode(a, "utf-8"))
        
        #Some RegEx Trainings
        #finding 'ler' and 'lar' in the word and inserting them in plurals array
        plurals = re.findall(r'\b\w*l[ea]r\w*\b', codecs.decode(a, "utf-8"))
        
        #finding nouns and inserting them in properNouns array
        properNouns = re.findall(r'\b[A-Z]\w*\b', codecs.decode(a, "utf-8"))
        
        #finding words
        words = re.findall(r'[^\s]+', codecs.decode(a, "utf-8"))
        
        #counting words
        wordCount += len(re.findall(r'[^\s]+', codecs.decode(a, "utf-8")))
        print(plurals)
        print(properNouns)
        for word in words:
            wordLength += str(word).__len__()
    print(wordCount)
    print(wordLength)
    average = wordLength / wordCount
    print("%.2f" % average)
    file.close()
