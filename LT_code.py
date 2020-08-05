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
        for i in range(self.n):
            selection_indexes = self.sample_indexes(i, self.random_degrees[i])
            self.list_indexes.append(selection_indexes)
            self.list_degrees.append(self.random_degrees[i])

        self.backup_list_indexes = copy.deepcopy(self.list_indexes)
        self.backup_list_degrees = copy.deepcopy(self.list_degrees)
        print(max(self.list_degrees))
            #assert len(selection_indexes) == self.random_degrees[i]


    def construct_symbols(self, aggregated_result):
        #The aggregated result is [[index, matRes], [index, matRes], [index, matRes]]
        #self.construct_degrees_indexes()
        self.list_indexes = copy.deepcopy(self.backup_list_indexes)
        self.list_degrees = copy.deepcopy(self.backup_list_degrees)
        print(max(self.list_degrees))
        symbols=[]
        for data in aggregated_result:
            for i in range(data[1].shape[0]):

                #print(data[1].shape[0])
                index=data[0][0]+i
                #if(index == 4000):
                    #print('error is', data[0][0], index)
                symbol = Symbol(index, self.list_degrees[index], data[1][i,:], self.list_indexes[index])
                symbols.append(symbol)
                #print(data[1].shape[0],index, symbol.data, symbol.degree, symbol.neighbors, self.list_indexes )
                #print('symbol index %d' %index, symbol.degree, symbol.neighbors)
        return symbols


    def lt_decode(self, aggregared_result):

        start_time = time.time()
        symbols = self.construct_symbols(aggregared_result)
        #print(len(symbols))
        end_time = time.time()
        print('construct_symbols done', end_time - start_time)
        num_symbols = len(symbols)
        recovered_count = 0
        Ax = [None] * self.m
        #print('Recovered candidate Ax', Ax)
        iteration_solved_count = 0
        while iteration_solved_count > 0 or recovered_count == 0:
            iteration_solved_count = 0
            print('1')
            for i, symbol in enumerate(symbols):
                if symbol.degree == 1:
                    #print('Index is', symbol.index)
                    #print('Neighbor', symbol.neighbors)
                    iteration_solved_count += 1
                    #print(symbol.neighbors)
                    index = symbol.neighbors[0]
                    symbols.pop(i)
                    if Ax[index] is not None:
                        continue
                    Ax[index] = symbol.data
                    self.reduce_neighbors(index, Ax, symbols)
                    recovered_count += 1
        print('Recovered_count is', recovered_count)

        return Ax

    def reduce_neighbors(self, index, Ax, symbols):
        for other_symbol in symbols:
            if other_symbol.degree > 1 and index in other_symbol.neighbors:
                other_symbol.data = other_symbol.data-Ax[index]
                other_symbol.neighbors.remove(index)
                other_symbol.degree -= 1
        return



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
