import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Question 2

(nmax,mu,sigma) = (100,0,0.5)
tv = [10,20,50,100,200]
nv = [1,2,3,5,10]

# part 1
temp = np.zeros((nmax,len(tv),len(nv)))
for ndx,n in enumerate(nv):
    for tdx,T in enumerate(tv):
        for imax in range(nmax):
            e = np.random.normal(mu,sigma,size=(T+1,1))
            y = np.random.normal(mu,sigma,size=(T+1,1))
            for t in range(1,T+1):
                y[t] = y[t-1] + e[t]
            y = y[1:]    
            u = np.random.normal(mu,sigma,size=(T+1,n))
            x = np.random.normal(mu,sigma,size=(T+1,n))
            for t in range(1,T+1):
                for i in range(0,n):
                    x[[t],[i]] = x[[t-1],[i]] + u[[t],[i]]
            x = x[1:]
            x = sm.add_constant(x)
            model1 = smf.OLS(y,x).fit()
            temp[imax,tdx,ndx] = model1.rsquared
print(temp.mean(0))

# part 2
temp = np.zeros((nmax,len(tv),len(nv)))
for ndx,n in enumerate(nv):
    for tdx,T in enumerate(tv):
        for imax in range(nmax):
            y = np.random.normal(mu,sigma,size=(T,1))
            x = np.random.normal(mu,sigma,size=(T,n))
            x = sm.add_constant(x)
            model2 = smf.OLS(y,x).fit()
            temp[imax,tdx,ndx] = model2.rsquared
print(temp.mean(0))

print('')

# Question 3

(T,mu,sigma) = (100,0,0.5)
df = pd.DataFrame(np.random.normal(mu,sigma,size=(T+1,1)),columns=list('y'))
for p in (-0.75,-0.5,-0.25,0,0.25,0.5,0.75):
    for i in range(1,T+1): df['y'][i] += p*df['y'][i-1]
    df['y_t'] = df['y'][1:T+1]
    df['y_tminus1'] = df.y.shift(1)
    df_data = df.drop(index=0,columns='y')
    ols0 = smf.ols('y_t~y_tminus1-1',data=df_data).fit()
    ols1 = smf.ols('y_t~y_tminus1',data=df_data).fit()
    output = [[p],[ols0.params[0]],[ols0.bse[0]**2],[ols1.params[1]],[ols1.bse[1]**2],[ols0.params[0]-ols1.params[1]]]
    df_out = pd.DataFrame(output)
    df_out['Results'] = ['rho','no constant b1','no constant var(b1)','with constant b1','with constant var(b1)','bias']
    df_out = df_out.set_index('Results')
    print(df_out)
print('\nAs the absolute value of rho becomes close to 1, the bias is increasing')