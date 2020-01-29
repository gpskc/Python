import time as tm
import pandas as pd

## part 1 ##

t1 = tm.time()
limit = 1000
m = 1000
a = 10
b = 10
list = []

for a in range(1,a+1):
    for b in range(1,b+1):
        bad = 0
        for i in range(1,m+1):
            if bad > 0: break
            cycles = 0
            x = i
            while x >= 1:
                if x == 1: break
                if x % 2 == 0: x //= 2
                else: x = a*x + b
                cycles += 1
                if cycles == limit:
                    bad += 1
                    break
            list += [[a,b,i,cycles]]

df1 = pd.DataFrame(list,columns=['a','b','x','cycles'])
df1['maxcycles'] = df1.groupby(['a','b'])['cycles'].transform('max')
df1 = df1.query('cycles > 0 and maxcycles < 1000')
df1 = df1[['a','b','cycles']].drop_duplicates()
df1 = df1.groupby(['a','b']).count()
print("Max number of iterations allowed for the series to converge =",limit)
print("Following",df1.shape[0],"a,b pairs converged to 1 for x in the range of 1 to 1000")
print("Execution Time",round(tm.time()-t1,2),"seconds")
print(df1)

## part 2 ##

t2 = tm.time()
limit = 1000
m = 1000
a1 = 10
a2 = 10
b1 = 10
b2 = 10
list = []

for a1 in range(1,a1+1):
    for a2 in range(1,a2+1):
        for b1 in range(1,b1+1):
            for b2 in range(1,b2+1):
                bad = 0
                for i in range(1,m+1):
                    if bad > 0: break
                    cycles = 0
                    x = i
                    while x >= 1:
                        if x == 1: break
                        if x % 3 == 0: x //= 3
                        elif x % 3 == 1: x = a1*x + b1
                        elif x % 3 == 2: x = a2*x + b2
                        cycles += 1
                        if cycles == limit:
                            bad += 1
                            break
                    list += [[a1,a2,b1,b2,i,cycles]]

df2 = pd.DataFrame(list,columns=['a1','a2','b1','b2','x','cycles'])
df2['maxcycles'] = df2.groupby(['a1','a2','b1','b2'])['cycles'].transform('max')
df2 = df2.query('cycles > 0 and maxcycles < 1000')
df2 = df2[['a1','a2','b1','b2','cycles']].drop_duplicates()
df2 = df2.groupby(['a1','a2','b1','b2']).count()
print("Max number of iterations allowed for the series to converge =",limit)
print("Following",df2.shape[0],"a1,a2,b1,b2 pairs converged to 1 for x in the range of 1 to 1000")
print("Execution Time",round(tm.time()-t2,2),"seconds")
print(df2)

