def ngram(list, n):
    result = []
    for i in range(len(list) - n + 1):
        result.append(list[i:i + n])
    return result


stc = 'I am an NLPer'
print(ngram(stc, 2))

words = stc.split()
print(ngram(words, 2))
