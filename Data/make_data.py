# -*- coding: utf-8 -*-
import numpy as np
import random
random.seed(0)

def generate_probability_array(num_of_size):
    res = []
    for i in range(num_of_size):
        p_1 = random.randint(0, 10)
        p_2 = random.randint(0, 15)
        p_5 = random.randint(0, 20)
        p_3 = random.randint(0, 100 - p_1 - p_2 - p_5)
        p_4 = 100 - p_1 - p_2 - p_3 - p_5
        print('{}: 1: {} 2: {} 3: {} 4: {} 5: {}'.format(i, p_1, p_2, p_3, p_4, p_5))
        res.append([
            p_1,
            p_1 + p_2,
            p_1 + p_2 + p_3,
            p_1 + p_2 + p_3 + p_4,
            100
        ])
    return res

def generate_form(probability):
    form = np.zeros((9, 39))
    for i in range(9):
        for k in range(39):
            r = random.randint(1, 100)
            for j in range(len(probability)):
                if r <= probability[j]:
                    form[i, k] = j + 1
                    break
    return form

if __name__ == "__main__":
    probability_arr = generate_probability_array(20)
    for i in range(len(probability_arr)):
        form = generate_form(probability_arr[i])
        with open('car_{}.txt'.format(i), 'w') as f:
            f.write(str(form))
            f.close()


