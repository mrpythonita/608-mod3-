# importing necessary modules
from collections import Counter
import numpy as np
random_dice_roll = np.random.randint(1,7,size=6_000_000)
results= Counter(random_dice_roll)
for key,value in sorted(results.items()):
    print('Face: {} Frequency: {}'.format(key,value))
