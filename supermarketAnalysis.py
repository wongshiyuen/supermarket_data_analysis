import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import ttest_ind
#=======================================================================================================
#Dataset
path = r"C:\Users\Wong Shi Yuen\OneDrive\Documents\supermarketSales\supermarket_sales new.csv"
df = pd.read_csv(path)

#Hypothesis testing threshold
#Common value = 0.05
threshold = 0.05
#=======================================================================================================
#TEST 1 (ONE-TAILED T-TEST)
#-------------------------------------------------------------------------------------------------------
#Identify mean and standard deviation of spending for 'normal' customers.
normalMaskedData = df[df['Customer type']=='Normal']
normalSales = normalMaskedData['Unit price']
normalMeanSales = np.mean(normalSales)
normalStdSales = np.std(normalSales)

#Identify mean and standard deviation of spending for 'member' customers.
memberMaskedData = df[df['Customer type']=='Member']
memberSales = memberMaskedData['Unit price']
memberMeanSales = np.mean(memberSales)
memberStdSales = np.std(memberSales)
#-------------------------------------------------------------------------------------------------------
H0 = "No difference in sales between 'normal' and 'member' customers."
H1 = "Significantly higher sales from 'normal' customers."
H2 = "Significantly higher sales from 'member' customers."

#Perform Welch’s one-tailed t-test (does not assume equal variance)
#tStat = the gap measured in standard units.
#pVal = chance of extreme value if there were no real difference; higher chance = closer distribution.
tStat, pVal = ttest_ind(normalSales, memberSales, equal_var=False)
pVal = pVal/2 #Convert to p-value for one-tailed testing
#-------------------------------------------------------------------------------------------------------
#Results
print(f"'Normal' sales: Mean = {normalMeanSales}, Std. dev. = {normalStdSales}")
print(f"'Member' sales: Mean = {memberMeanSales}, Std. dev. = {memberStdSales}")

print(f"t-statistic = {tStat}, p-value = {pVal}")
#Convert to one-tailed testing
if pVal < threshold:
    if tStat > 0:
        print(H1) #normalSales mean > memberSales mean
    else:
        print(H2) #normalSales mean < memberSales mean
else:
    print(H0)
#=======================================================================================================
#TEST2: ONE-WAY ANOVA ON UNIT PRICE BY BRANCH
#-------------------------------------------------------------------------------------------------------
model = ols('Q("Unit price") ~ C(Branch)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)
#=======================================================================================================