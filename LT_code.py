import numpy as np
import math
import random
import time
import copy

random.seed(30)
np.random.seed(30)

class Symbol:
    def __init__(self, index, degree, data, neighbors):
        self.index = index
        self.degree = degree
        self.data = data
        self.neighbors = neighbors


class LT_Code():
    def __init__(self, delta, c, m, n):
        self.delta = delta
        self.c = c
        self.m = m
        self.n = n

        # Set the random seed

        self.construct_degrees_indexes()

    def sample_indexes(self, symbol_index, degree):
        random.seed(symbol_index)
        indexes = random.sample(range(self.m), degree)
        return indexes

    def get_degrees (self):
        prob_d = self.robust_soliton_distribution()
        population = list(range(1,self.m+1))
        return np.random.choice(population, self.n, p=prob_d)#random.choices(population, prob_d, k=self.n)

    def robust_soliton_distribution(self):
        R = self.c*math.log(self.m/self.delta)*math.sqrt(self.m)
        rho_d = []
        rho_d = [R/(1*self.m)+1/self.m] # d=1
        #print(len(rho_d))
        rho_d += [R/(d*self.m)+1/(self.m*(self.m-1)) for d in range(2, int(np.ceil(self.m/R)))]
        #print(len(rho_d))
        rho_d += [R*math.log(R/self.delta)/self.m+1/(self.m*(self.m-1)) for d in range(int(np.ceil(self.m/R)),int(np.ceil(self.m/R))+1)]
        #print(len(rho_d))
        rho_d += [1/(self.m*(self.m-1)) for d in range(int(np.ceil(self.m/R))+1, self.m+1)]
        rho_sum = sum(rho_d)
        #print(len(rho_d))
        #print(int(self.m/R))
        prob_d = [rho_d[i]/rho_sum for i in range(self.m)]
        #print(sum(prob_d))
        return prob_d

    def construct_degrees_indexes(self):
        self.random_degrees = self.get_degrees()
        #print(self.random_degrees)
        #print(self.random_degrees)
        self.list_indexes =[]
        self.list_degrees =[]
        self.list_checknode_indexes = []


        for i in range(self.n):
            selection_indexes = self.sample_indexes(i, self.random_degrees[i])
            self.list_indexes.append(selection_indexes)
            self.list_degrees.append(self.random_degrees[i])


        for i in range(self.m):
            index = []
            for j, variable_index in enumerate(self.list_indexes):
                if i in variable_index:
                    index.append(j)
            self.list_checknode_indexes.append(index)



        self.backup_list_indexes = copy.deepcopy(self.list_indexes)
        self.backup_list_degrees = copy.deepcopy(self.list_degrees)
        self.backup_list_checknode_indexes = copy.deepcopy(self.list_checknode_indexes)
            #assert len(selection_indexes) == self.random_degrees[i]


    def lt_decode(self, aggregated_result):

        self.list_indexes = copy.deepcopy(self.backup_list_indexes)
        self.list_degrees = copy.deepcopy(self.backup_list_degrees)
        self.check_indexes = copy.deepcopy(self.backup_list_checknode_indexes)

        #print(self.list_indexes)

        received_index = [data[1] for data in aggregated_result]


        for index in self.check_indexes:
            for item in index:
                if item not in received_index:
                    index.remove(item)

        Ax = [None] * self.m

        count = 0
        recovered = 0
        while True:
            count += 1
            for data in aggregated_result:
                    index=data[1]
                    variable_index = copy.deepcopy(self.list_indexes[index])
                    if(len(variable_index) == 1 and Ax[variable_index[0]] is None):
                        count = 0
                        recovered += 1
                        Ax[variable_index[0]] = data[0]

                        for item in self.check_indexes[variable_index[0]]:
                            if len(self.list_indexes[item])>1:
                                #print(self.check_indexes[variable_index[0]], variable_index, variable_index[0], item, index)
                                #print(self.list_indexes[item])
                                self.list_indexes[item].remove(variable_index[0])

                                item_index = received_index.index(item)
                                aggregated_result[item_index][0] -=  data[0]
            if(count>=1):
                break
        print('Recovered result', recovered)

        return Ax




if __name__== '__main__':
    pass




# def recover_graph(aggregated_result):
#     random_degrees = get_degrees()
#     list_indexes =[]
#     list_degrees =[]
#     for i in range(n):
#         selection_indexes = sample_indexes(i, random_degrees[i], m)
#         list_indexes.append(selection_indexes)
#         list_degrees.append(random_degrees[i])
#
#
#     for data in aggregated_result:
#         data.append(list_indexes[data[0][0], data[0][1]], list_degrees[data[0][0], data[0][1]])
#
#     return aggregated_result


# def encode(A_matrix):
#
#     random_degrees = get_degrees()
#
#     encoded_A_symbol=[]
#     for i in range(m):
#         selection_indexes = sample_indexes(i, random_degrees[i], m)
#
#         encoded_row = np.sum(A_matrix[selection_indexes, :])
#         symbol = Symbol(index=i, random_degrees[i], encoded_row)
#         encoded_A_symbol.append(symbol)
#
#     return encoded_A_symbol
