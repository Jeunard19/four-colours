adj = [
    [ 0, 1, 1, 1, 0 ],
    [ 1, 0, 1, 0, 0 ],
    [ 1, 1, 0, 1, 0 ], 
    [ 1, 0, 1, 0, 1 ], 
    [ 0, 0, 0, 1, 0 ]  
]


colors = [1,2,3,4]

results = {"A":1,"B":1,"C":1,"D":1,"E":1}
mapps = {}
letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for s,i in enumerate(adj):
	key = letters[s]
	mapps[key] = []
	for k,x in enumerate(i):
		if x == 1:
			border = letters[k]
			mapps[key].append(border)

count=0
print(mapps)
for key, value in mapps.items():
	print(value)
	for i in value:
		if results[key] == results[i]:
			try:
				count+=1
				results[key] = colors[count]
			except IndexError:
				count=0
				results[key] = colors[count]

print(results)





