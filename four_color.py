adj = [
    [ 0, 1, 1, 1, 0 ],
    [ 1, 0, 1, 0, 0 ],
    [ 1, 1, 0, 1, 0 ], 
    [ 1, 0, 1, 0, 1 ], 
    [ 0, 0, 0, 1, 0 ]  
]

adj = [
    [0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0]
]

adj = [
    [0, 1, 0, 1, 0, 1],  # A
    [1, 0, 1, 1, 0, 0],  # B
    [0, 1, 0, 0, 1, 0],  # C
    [1, 1, 0, 0, 1, 0],  # D
    [0, 0, 1, 1, 0, 1],  # E
    [1, 0, 0, 0, 1, 0]   # F
]





colors = [1,2,3,4]


mapps = {}


for s,i in enumerate(adj):
	key = f"Region_{s}"
	mapps[key] = []
	for k,x in enumerate(i):
		if x == 1:
			border = f"Region_{k}"
			mapps[key].append(border)

results = {}
for key, value in mapps.items():
	results[key] = 1



count=0
for key, value in mapps.items():
	for i in value:
		if results[key] == results[i]:
			try:
				count+=1
				results[key] = colors[count]
			except IndexError:
				count=0
				results[key] = colors[count]
print(mapps)
print(results)





