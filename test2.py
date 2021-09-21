import sys 
act = sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])
key = {
'add' : a + b,
'substract' : a - b,
'multiply' : a * b,
'divide' : a / b
}
print(key[act])


