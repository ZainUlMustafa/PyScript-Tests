import numpy as np
        
def sum(a, b):
    return a+b
#enddef

result = sum(10, 14)

numArr = np.array([10, 14, 12, -1])

pyscript.write('arr-output', f'Original: {numArr}, Sorted:')
pyscript.write('output' ,f'Result is: {result}')