from textblob import TextBlob

word = ['data scinece', 'aple', 'machin leraninn', 'artificila inteligence']

correct = []

for i in word:
    correct.append(TextBlob(i))

print("Wrong words: ", word)
print("Corrected words: ")
for i in correct:
    print(i.correct(),end=",")