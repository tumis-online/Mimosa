import de_core_news_sm


text = "Dies ist ein Satz."
nlp = de_core_news_sm.load()
doc = nlp(text)
print([(w.text, w.pos_) for w in doc])

for token in doc:
    print(token.text, token.pos_, token.dep_)

