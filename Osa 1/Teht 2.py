import numpy as np

print('#1')
a = 1.2
b = 2.3
hypo = round(np.hypot(a, b), 2)
print(f'Jos suorankulmion katetit ovat {a} ja {b}, sen hypotinuusa on {hypo}')