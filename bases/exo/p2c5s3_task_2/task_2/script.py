import nltk

nltk.download('punkt')

sentence = 'Open Classrooms is an excellent online learning provider'
tokens = nltk.word_tokenize(sentence)
print('By using NLTK tokenization on the sentence...')
print(sentence)
print('We get...')
print(tokens)

