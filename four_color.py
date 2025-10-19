from pyvis.network import Network
import networkx as nx
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

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






colors = [1,2,3,4]


mapps = {}
g = Network()


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

vis_colors =["red","green","blue","yellow"]
print(vis_colors[1])

true_colors = [vis_colors[(x-1)] for x in list(results.values())]
print(true_colors)
nodes=list(results.keys())
net.add_nodes(nodes,color=true_colors) 
print(list(results.values()))
for key, value in mapps.items():
	for i in value:
		net.add_edge(key,i)




g = Network()
#g.add_node(0)
#g.add_node(1)
#g.add_edge(0, 1)
net.show('test.html', notebook=False)



