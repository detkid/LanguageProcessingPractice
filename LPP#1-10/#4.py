stc = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = stc.split()

ans = ''
for word in words:
    ans += str(len(word))

print(ans)
