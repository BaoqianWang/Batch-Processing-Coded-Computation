import math

delta = 0.001
c = 0.02
m = 1000
n = 1500



R = c*math.log(m/delta)*math.sqrt(m)

print(int(m/R)+1)

rho_d = []
rho_d = [R/(1*m)+1/m] # d=1
rho_d += [R/(d*m)+1/(m*(m-1)) for d in range(2, int(m/R))]
rho_d += [R*math.log(R/delta)/m+1/(m*(m-1)) for d in range(int(m/R),int(m/R)+1)]
rho_d += [1/(m*(m-1)) for d in range(int(m/R)+1, m+1)]

rho_sum = sum(rho_d)
prob_d = [rho_d[i]/rho_sum for i in range(m)]
print(prob_d)
print(sum(prob_d))
print(len(rho_d))

for d in range(int(m/R),int(m/R)):
    print(d)
