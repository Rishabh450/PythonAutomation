message = input(">")
words = message.split(' ')
#print(words)
emoji = {
    ":)": "😀" ,
    ":(": "😟"

}
sent = ""
for word in words:
    if emoji.get(word) is None:
        sent = sent + word + " "
    else:
        sent = sent + emoji[word]
print(sent)
