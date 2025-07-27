f = open("poem.txt")
c = f.read()
if("twinkle" in c):
    print("Twinkle is present in the content")
else:
    print("Twinkle is not present in the content")
f.close()