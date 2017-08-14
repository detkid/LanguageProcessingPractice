stc = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = stc.split()

dict = {}
for (i, word) in enumerate(words):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dict[word[0]] = str(i)
    else:
        dict[word[0] + word[1]] = str(i)

print(dict)
