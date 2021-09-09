# AskZote
## Introduction
In the game, Hollow Knight, the character Zote famously shares invaluable life advice to the player through 57 precepts. Using those 57 precepts as "answers", AskZote queries the user for a question and returns the most relevant precept. Relevance is defined as the closest precept to the words in the input question based on a word2vec model trained on the [text8](http://mattmahoney.net/dc/textdata.html) corpus.
