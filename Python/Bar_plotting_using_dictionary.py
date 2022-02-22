import matplotlib.pyplot as plt
def punctuation_removal(s):
    s = s.lower()
    punc = '''!()-[]{};: '"\,<>./?@#$%^&*_~'''
    a = []
    a[:] = s
    b = []
    for i in a:
        if i in punc:
            b.append(i)
        else:
            pass
    for l in b:
        a.remove(l)
    return a
def histogram(q):
    p = punctuation_removal(q)
    dict1 = {}
    dict2 = {}
    for i in p:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    for i in (sorted(dict1.keys())):
        dict2[i] = dict1[i]
    return dict2

string = str(input('Give me some sentence : '))
#string = 'Heloo Pinky.!! How are you.?? ? Howzz your preparation going??'
c = histogram(string)
plt.bar(c.keys(),c.values(), width=0.5, color = 'g')
plt.show()
