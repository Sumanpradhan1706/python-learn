word = "Donkey"

with open("word.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("word.txt", "w") as f:
     f.write(contentNew)
