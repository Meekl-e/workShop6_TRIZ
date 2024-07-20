from gensim.models import KeyedVectors


model = KeyedVectors.load_word2vec_format('model.bin', binary=True)


print(model.most_similar(positive=["король_NOUN", "женщина_NOUN"], negative=["мужчина_NOUN"], topn=5))

print("ready")
while True:
   word = input()
   #negative = input()
   if word in model:
       for i in model.most_similar(positive=[word], topn=10):
           print(i[0], i[1])
       print('\n')
   else:

       print(word + ' NOT IN MODELL')