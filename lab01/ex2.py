# Błąd obcięcia

import numpy as np

a = np.float32(0.1)
b = np.float32(0.2)

print(0.1 + 0.2 == 0.3) # Wrong! Do not compare floating point numbers like this
# False
print(a + b - np.float32(0.2))
# 0.10000001

print(0.1+0.2)
