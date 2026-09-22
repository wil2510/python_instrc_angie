temperaturas = [18, 22, 25, 19, 30]

fahrenheit = [
    temperatura * 9 / 5 + 32
    for temperatura in temperaturas
]

print(fahrenheit)