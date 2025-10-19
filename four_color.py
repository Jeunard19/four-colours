#!/usr/bin/venv python3
from pyvis.network import Network


def create_bording_region_dict(adj):
	bording_region_dict= {}
	for s,i in enumerate(adj):
		key = f"Region_{s}"
		bording_region_dict[key] = []
		for k,x in enumerate(i):
			if x == 1:
				region = f"Region_{k}"
				bording_region_dict[key].append(region)
	return bording_region_dict

def create_initial_results_dict(bording_region_dict):
	results = {}
	for key, value in bording_region_dict.items():
		results[key] = 1
	return results

def allocate_color(bording_region_dict, results_dict, minimize=False):
	colors = [1,2,3,4]
	count=0
	regions = list(bording_region_dict.keys())
	for key, value in bording_region_dict.items():
		# This is for minimizing color use
		if minimize:
			non_bording_regions = [i for i in regions if i not in value]
			for region in non_bording_regions:
				if results_dict[key] != results_dict[region]:
					results_dict[key]=results_dict[region]
		
		for i in value:
			if results_dict[key] == results_dict[i]:
				try:
					count+=1
					results_dict[key] = colors[count]
				except IndexError:
					count=0
					results_dict[key] = colors[count]
	return results_dict


def create_connected_node_network(bording_region_dict, results_dict):
	net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
	vis_colors =["red","green","blue","yellow"]
	selected_colors = [vis_colors[(x-1)] for x in list(results_dict.values())]
	
	nodes=list(results_dict.keys())
	net.add_nodes(nodes,color=selected_colors) 
	
	for key, value in bording_region_dict.items():
		for i in value:
			net.add_edge(key,i)
	net.show('map.html', notebook=False)



def main():
    adj = [
        [ 0, 1, 1, 1, 0 ],
        [ 1, 0, 1, 0, 0 ],
        [ 1, 1, 0, 1, 0 ], 
        [ 1, 0, 1, 0, 1 ], 
        [ 0, 0, 0, 1, 0 ]  
    ]
    adj = [
    [0, 1, 1, 0, 0, 0, 0],  # Node 0
    [1, 0, 1, 1, 0, 0, 0],  # Node 1
    [1, 1, 0, 0, 1, 0, 0],  # Node 2
    [0, 1, 0, 0, 1, 1, 0],  # Node 3
    [0, 0, 1, 1, 0, 0, 1],  # Node 4
    [0, 0, 0, 1, 0, 0, 1],  # Node 5
    [0, 0, 0, 0, 1, 1, 0]   # Node 6
]
    adj = [
    [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],  # 0
    [1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],  # 1
    [1,1,0,0,1,0,0,0,0,0,0,0,0,0,0],  # 2
    [0,1,0,0,1,1,0,0,0,0,0,0,0,0,0],  # 3
    [0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],  # 4
    [0,0,0,1,0,0,1,1,0,0,0,0,0,0,0],  # 5
    [0,0,0,0,1,1,0,1,1,0,0,0,0,0,0],  # 6
    [0,0,0,0,0,1,1,0,1,1,0,0,0,0,0],  # 7
    [0,0,0,0,0,0,1,1,0,1,1,0,0,0,0],  # 8
    [0,0,0,0,0,0,0,1,1,0,1,1,0,0,0],  # 9
    [0,0,0,0,0,0,0,0,1,1,0,1,1,0,0],  # 10
    [0,0,0,0,0,0,0,0,0,1,1,0,1,1,0],  # 11
    [0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],  # 12
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],  # 13
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0]   # 14
]





    

    

    bording_region_dict = create_bording_region_dict(adj)
    initial_results_dict = create_initial_results_dict(bording_region_dict)
    result_dict = allocate_color(bording_region_dict, initial_results_dict, True)
    
    
    for region, color in result_dict.items():
        print(f"{region}  Color {color}")

    create_connected_node_network(bording_region_dict, result_dict)

if __name__ == "__main__":
	main()


