import numpy as np
from scipy import stats
data = np.random.normal(0,1,1000)
#Normal Distribution
#Calculating basic statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
skewness = stats.skew(data)
kurt = stats.kurtosis(data)
print(mean)
print(median)
print(std_dev)
print(skewness)
print(kurt)
#performing t-test - 1 sample t-test
# t_statistic, p_value = stats.ttest_1samp(data,0)
# print(f"T-statistic: {t_statistic}")
# print(f"P-value: {p_value}")
t_statistic,p_value=stats.ttest_1samp(data,0)
print(f"T-statistics:{t_statistic}")
print(f"P-value:{p_value}")
# mean and median not equal so, not a normal distribution
# skewness-slope(normal dist --> left and right are symmetric, mean, median are same)
# When skewness and kurtsosis are close to zero, it is considered a normal distribution
# standard deviation - how the value are distributed
# skewness - A skewness value between -1 and +1 is generally acceptable for normal distribution
# Values between -1 and -0.5 or between +0.5 and +1 might be moderately skewed
# Values less than -1 or greater than +1 are typically regarded as highly skewed
# Null Hypothesis - saying its gonna be same (generally accepted, common sense statements)
# Alternate Hypothesis - going to be differnt, Eg: class average will be different from district average
# It opposes the Null Hypothesis
#use of null hypothesis in criminal proceedings
#Eg: null hyptothesis is innocent
#Alternate hypothesis is not innocent (oppposite of null hypothesis)
#Null hypothesis is the coomon statement
#Scipy statisticsl significance tests
#whenever the pvalue is greater than 0.05 we have to accept the null hypothesis, else accept the alternate hypothesis
#help(stats.ttest_1samp)
sample1 = np.random.normal(0,1,1000)
sample2 = np.random.normal(0.5,1,1000)
#performing t-test - 2 sample test
#Eg: Horlicks survey on men and women, sample1-men, sample2-women
t_statistic2 , p_value2 = stats.ttest_ind(sample1, sample2) 
print(t_statistic2)
print(p_value2)
#try for tooth growth sample
#checking whether orange juice is better or the vitamin supplements
#Perform Kolmogorov-Smirnov test: