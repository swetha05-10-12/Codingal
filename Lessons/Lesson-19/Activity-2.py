def match_words(words):
    ctr=0
    lst=["abc","cfc","xyz","aba",12231]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr+=1
            lst.append
    print("The list of words that start and end with the same character",lst)
    return ctr

count=match_words(["abc","cfc","xyz","aba","12231"])
print("Number of words starting and ending with the same character:",count)