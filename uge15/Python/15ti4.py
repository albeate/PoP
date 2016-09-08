import codecs

fh = codecs.open("ugeseddel_data.txt", encoding = "utf-8")

text = fh.read()

print type(text)

print text.encode('utf-8')
