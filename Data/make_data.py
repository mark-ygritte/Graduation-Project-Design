# -*- coding: utf-8 -*-
import numpy as np
import random
# random.seed(1)

def generate_probability_array(num_of_size):
    res = []
    for i in range(num_of_size):
        p_1 = random.randint(0, 20)
        p_2 = random.randint(0, 20)
        p_5 = random.randint(0, 40)
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
    form = np.zeros((39, 9))
    for i in range(9):
        for k in range(39):
            r = random.randint(1, 100)
            for j in range(len(probability)):
                if r <= probability[j]:
                    form[k, i] = j + 1
                    break
    return form

def get_pro(pro, fre):
    def judge(pro):
        if pro < 3.0:
            if random.randint(0, 100) <= 70:
                return 1
            else:
                return 0
        elif pro < 3.2:
            if random.randint(0, 100) < 50:
                return 1
            else:
                return 0
        elif pro < 3.4:
            if random.randint(0, 100) < 30:
                return 1
            else:
                return 0
        elif pro < 3.6:
            if random.randint(0, 100) < 25:
                return 1
            else:
                return 0
        elif pro < 3.8:
            if random.randint(0, 100) < 15:
                return 1
            else:
                return 0
        elif pro < 4.0:
            if random.randint(0, 100) < 10:
                return 1
            else:
                return 0
        elif pro < 4.5:
            if random.randint(0, 100) < 2:
                return 1
            else:
                return 0
        elif pro < 5:
            if random.randint(0, 100) < 1:
                return 1
            else:
                return 0
    
    res = []
    if fre == 5:
        n = random.randint(100, 200)
    elif fre == 4:
        n = random.randint(50, 150)
    elif fre == 3:
        n = random.randint(50, 100)
    elif fre == 2:
        n = random.randint(25, 75)
    elif fre == 1:
        n = random.randint(10, 50)
    
    for i in range(n):
        res.append(judge(pro))
    
    return res

if __name__ == "__main__":
    # Generate form
    # probability_arr = generate_probability_array(20)
    # for i in range(len(probability_arr)):
    #     form = generate_form(probability_arr[i])
    #     with open('./forms/car_{}.txt'.format(i), 'w') as f:
    #         f.write(str(form))
    #         f.close()

    # Generate occur probability
    weight_dict = {
        'server': ([0, 10], 10.0 / 42),
        'network': ([10, 15], 10.0 / 42),
        'database': ([15, 22], 7.0 / 42),
        'application': ([22, 29], 9.0 / 42),
        't_management': ([29, 34], 4.0 / 42),
        'org': ([34, 39], 2.0 / 42)
    }

    frequnce_t = [
        [5, 2, 2, 4, 3, 4, 1],
        [4, 2, 3, 5, 2, 4],
        [1, 2, 1],
        [3, 5, 5],
        [1, 2, 1, 5, 5],
        [4, 3, 1, 2, 5, 2, 5, 5, 2, 4, 1],
        [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 3, 2, 3, 1, 1, 5],
        [1, 5, 4, 5, 5, 5, 2],
        [5, 2, 5, 3, 2, 3]
    ]
    
    car_vec = []

    events = []

    for i in range(20):
        with open('./forms/car_{}.txt'.format(i), 'r') as f:
            data = f.read().replace('.', ',').replace(']', '],')
            arr = eval(data)[0]
            f.close()
        res = []
        for h in range(9):
            count = 0.0
            for key in weight_dict.keys():
                r = weight_dict[key][0]
                weight = weight_dict[key][1]
                # print(weight)
                tmp = 0.0
                for j in range(*r):
                    tmp += arr[j][h]
                tmp = tmp / (r[1] - r[0]) * weight
                count += tmp
            res.append(count)
        car_vec.append(res)
    
        training_data = []

        for k in range(9):
            pro = car_vec[i][k]
            fre_l = frequnce_t[k]
            for j in range(len(fre_l)):
                item = fre_l[j]
                training_data.append([k, j, get_pro(pro, item)])
                # print(res)
        with open('./forms/car_{}_training.txt'.format(i), 'w') as f:
            f.write(str(training_data))
            f.close()

