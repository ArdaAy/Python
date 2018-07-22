import codecs
import re
import time

#finding words in a corpus and calculating bigram probabilities using that corpus
class NLP2:
    file = codecs.open("corpus.txt", "r", "utf-8")

    #Lines of corpus
    lines = []

    #All words
    allWords = re.findall(r'\w+', open('corpus.txt').read())

    for i in range(allWords.__len__()):
        allWords[i] = allWords[i].lower()

    # get lines
    for line in file:
        lines.append(line.encode("utf-8").lower())

    #Finding all unique words
    uniqueWords = []
    for i in range(allWords.__len__()):
        if allWords[i] not in uniqueWords:
            uniqueWords.append(allWords[i])

    for i in range(uniqueWords.__len__()):
        print(uniqueWords[i]+" : "+str(allWords.count(uniqueWords[i])))


    startTime = time.time()
    f = open("corpusProb.txt","w")
    #Prob of two words
    for i in range(uniqueWords.__len__()):
        startEnd = True
        for j in range(uniqueWords.__len__()):
            count = 0
            #if i != j:

            for line in lines:

                if startEnd:
                    start       = re.findall(r'^\b'+uniqueWords[i]+r'\b',codecs.decode(line,"utf-8"))
                    end         = re.findall(r'\b'+uniqueWords[i]+r'\b$',codecs.decode(line,"utf-8"))
                    probStart   = start.__len__()/lines.__len__()
                    textProbStart = "<s> "+uniqueWords[i]+" : "+ str(probStart)
                    probEnd     = end.__len__()/lines.__len__()
                    textProbEnd = "</s> "+uniqueWords[i]+" : "+ str(probEnd)
                    if probStart > 0:
                        print(textProbStart)
                    if probEnd > 0:
                        print(textProbEnd)
                    f.write(textProbStart+"\n"+textProbEnd+"\n")
                    startEnd = False
                test = re.findall(r'\b'+uniqueWords[i]+r'\b.\b'+uniqueWords[j]+r'\b',codecs.decode(line,"utf-8"))
                count = count + test.__len__()
            #prob = str(count) +"/"+ str(allWords.count(uniqueWords[i]));
            prob = count / allWords.count(uniqueWords[i])
            probText = uniqueWords[i]+" "+uniqueWords[j] +" : "+ str(prob)
            if prob > 0:
                print(probText)
            f.write(probText+"\n")

    f.close()
    endTime = time.time()
    print("Total Time Elapsed : "+str(endTime-startTime))
