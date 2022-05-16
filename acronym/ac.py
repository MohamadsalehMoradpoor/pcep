def user_input():
    i = input('Please Inter a Phrase: ')
    return i
def acronym(phrase):
    j = phrase.split()
    k = []
    for word in j:
        if len(word) <= 2:
            continue
        k.append(word[0])
    s = ""
    s = s.join(k)
    return s

ui = user_input()
a = acronym(ui)
print(a)