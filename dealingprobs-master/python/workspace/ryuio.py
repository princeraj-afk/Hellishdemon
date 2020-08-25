def alphabet_splitter(text):
    s = set()
    for i in range(len(text)):
        s.add(text[i:i+1])
    return len(text)**len(s)

def word_creator(text):
    s=set ()
    list1=[]
    for i in range (len (text)+1):
        for j in range (len (text)+1):
            if (i != j):
                s.add (text[i:j])
    return s

for i in range(int(input())):
    text = input()
    new_words = word_creator(text)
    no_of_new_words = len(new_words)
    new_words = list(new_words)
    num =0
    for i in range(no_of_new_words):
        if new_words[i] =="":
            pass
        else:
            num += alphabet_splitter(new_words[i])
    print(num%(10**9+7))