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
    [4, 3, 1, 2, 5, 2, 5, 2, 4, 1],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 2, 3, 1, 1, 5],
    [1, 5, 4, 5, 5, 5, 2],
    [5, 2, 5, 3, 2, 3]
]

training_data = [[] for i in range(65)]
labels = [[] for i in range(65)]

car_infos = [[] for i in range(9)]

for i in range(20):
    with open('./forms/car_{}.txt'.format(i), 'r') as f:
        car_info = f.read().replace('.', ',').replace(']', '],')
        car_info = eval(car_info)[0]
        car_info = np.asarray(car_info).T
        for k in range(9):
            for item in car_info[k]:
                car_infos[k].append(list(car_info[k]))
        f.close()

for i in range(20):
    with open('./forms/car_{}_training.txt'.format(i), 'r') as f:
        success_pro = eval(f.read())
        f.close()

    for item in success_pro:
#         module_id = item[0]
#         threat_id = item[1]
#         for e in item[2]:
#             car_module_info = list(car_info[module_id])
#             car_module_info.append(threat_id)
#             training_data[module_id].append(car_module_info)
#             labels[module_id].append(e)
    
# print(len(training_data[0]))
# print(len(labels[0]))
    
    

car_infos = np.asarray(car_infos)

print(car_infos.shape)