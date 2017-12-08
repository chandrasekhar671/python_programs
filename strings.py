sentence = "Using string methods in Jython is very he1pful. but you need to have a clear understanding of the method syntax and usage or e1se your jython program may fail complet1y. There is no wonder jython string methods are usefu1 in handling text properly"
words = sentence.split('. ')
capitalized_words = []
for i in words:
    title_case_word = i[0].upper() + i[1:]
    capitalized_words.append(title_case_word)
sentence = '. '.join(capitalized_words)
words = {'Jython':'python','jython':'python','1':'l','syntax':'SYNTAX','usage':'USAGE'}
for x,y in words.items():
    sentence = sentence.replace(x,y)
print(sentence)
    