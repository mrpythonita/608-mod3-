# Using the statistics module to calculate 
# measures of dispersion for a population. 
import statistics
import numpy as np
data = np.random.randint(1,7,size=6_000_000)
population_variance = statistics.pvariance(data)
population_std_deviation = statistics.pstdev(data)
print('The population variance for the dataset assigned is {} and population standard deviation is {}.'.format(population_variance,population_std_deviation))
