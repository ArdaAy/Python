#Arda Ay
#212CS2192
from __future__ import print_function
from collections import OrderedDict
import re
import codecs
class NLP3:
    cnt = 1
    wordList = []
    sentenceList = []
    with codecs.open("corpus.txt", "r", "utf-8") as fp:
        line = fp.readline()
        sentence = ""
        while line:

            if line.strip() == "":
                sentence = sentence[0:len(sentence)-1]
                sentenceList.append(sentence.lower())
                sentence = ""
            else:
                line = re.sub(r'[^\w\s]', '', line)
                if len(line) > 1:
                    sentence += line.strip() + " "
                    wordList.append(line)
            line = fp.readline()

    l = len(sentenceList)-1
    while l > 0:
        if sentenceList[l] == "":
            sentenceList.remove(sentenceList[l])
        l -= 1
    cnt = 0
    for item in sentenceList:
        print(item)
        cnt += 1
    print("SentenceList : "+str(len(sentenceList)))     #50659
    print("WordList : "+str(len(wordList)))             #730222

    released = {}
    for s in sentenceList:
        words = re.findall(r'\w+', s)
        for i, item in enumerate(words):
            contentList = []
            if released.get(words[i]) is not None:
                contentList = released.get(words[i])
            if i >= 2:
                contentList.append(words[i-2])
            if i >= 1:
                contentList.append(words[i-1])
            if i <= len(words) -2:
                contentList.append(words[i+1])
            if i <= len(words) -3:
                contentList.append(words[i+2])
            released[words[i]] = contentList

    for key in released:
        released[key] = list(OrderedDict.fromkeys(released.get(key)))

    similarity = {}

    for k1 in released:
        for k2 in released:
            if k1 != k2:
                cnt = 0
                v1 = []
                if released.get(k1) is not None:
                    v1 = released.get(k1)
                v2 = []
                if released.get(k2) is not None:
                    v2 = released.get(k2)
                for a1 in v1:
                    for a2 in v2:
                        if a1 == a2:
                            cnt += 1
                mth = cnt / (len(v1)+len(v2))
                similarity[k1+" - "+k2] = mth

    sortedList = OrderedDict(sorted(similarity.items(), key=lambda x: x[1],reverse=True))

    for i, z in enumerate(sortedList):
        print(z + " : "+str(sortedList[z]))
        if i > 20:
            break
    print(sortedList)
    #print(released)
    #print(similarity)
    # Approx number of process --> 730222^2 * 50659^2
    # My PC hasn't finished it
