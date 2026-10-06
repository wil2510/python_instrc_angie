import numpy as np

estudiantes = np.array([
    [4.8, 2.5, 3.3],    
    [5.0, 4.5, 3.8],    
    [4.0, 3.5, 4.2],    
    [3.2, 4.0, 3.5]     
])

print(estudiantes.mean(axis=0))
print(estudiantes.mean(axis=1))

                
