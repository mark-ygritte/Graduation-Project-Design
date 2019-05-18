# -*- coding: utf-8 -*-
import numpy as np
from sklearn.naive_bayes import MultinomialNB

X = np.random.randint(5, size=(6, 100))
y = np.array([1, 2, 3, 4, 5, 6])

clf = MultinomialNB()
clf.fit(X, y)
# MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
print(clf.predict(X[2:3]))

classifiers = []

frequnce_t = [
    [5, 2, 2, 4, 3, 4, 1],
    [4, 2, 3, 5, 2, 4],
    [1, 2, 1],
    [3, 5, 5],
    [1, 2, 1, 5, 5],
    [4, 3, 1, 2, 5, 2, 5, 5, 2, 4, 1],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 2, 3, 1, 1, 5],
    [1, 5, 4, 5, 5, 5, 2],
    [5, 2, 5, 3, 2, 3]
]

for i in range(20):
    with open('./forms/car_{}.txt'.format(i), 'r') as f:
        car_info = f.read().replace('.', ',').replace(']', '],')
        car_info = eval(car_info)[0]
        f.close()

    with open('./forms/car_{}_training.txt'.format(i), 'r') as f:
        training_data = eval(f.read())
        f.close()
    
    
