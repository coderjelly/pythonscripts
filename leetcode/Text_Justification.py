def fullJustify(words, L):
        l = len(words)
        finallist = []
        currList = []
        counter = 0
        i = 0
        while i < l:
            thislen = len(words[i])
            if L >= (counter + len(currList) + thislen):
                currList.append(words[i])
                counter += thislen
            else:
                if len(currList) > 1:
                    spaces = int((L - counter)/(len(currList) - 1))
                    xtra = int((L - counter)%(len(currList) - 1))
                    thisstr = currList[0] + " "*(spaces+xtra) + ((" "*spaces).join(currList[1:]))
                else:
                    spaces = L - counter
                    thisstr = " ".join(currList) + " "*(spaces - len(currList)+1)
                finallist.append(thisstr)
                counter = thislen
                currList = [words[i]]
            i += 1
        if len(currList) == 1:
                thislen = len(currList[0])
                finallist.append(currList[0]+" "*(L-thislen))      
        return finallist


words = ["Here","is","an","example","of","text","justification."]
L = 14

print fullJustify(words,L)