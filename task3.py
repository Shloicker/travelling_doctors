import doctor as dr
import networkx as nx
import matplotlib.pyplot as plt
import task2

def draw_solution(S, sol="Original"):
	G = nx.DiGraph()
	for n in range(dr.N):
		G.add_node(n, pos=dr.coords[n])

	edges = []
	for i in range(dr.n1):
		route = []
		for j in range(len(S[i])):
			if j == 0:
				edge = [i, S[i][j] + dr.n1]
				route.append(edge)
			elif j > 0:
				edge = [S[i][j-1] + dr.n1, S[i][j] + dr.n1]
				route.append(edge)
			if j == len(S[i]) - 1:
				edge = [S[i][j] + dr.n1, i]
				route.append(edge)
		edges.append(route)

	f = plt.figure()
	nx.draw_networkx_nodes(G, pos=nx.get_node_attributes(G, "pos"), nodelist=[node for node in range(dr.n1)], node_color="b")
	nx.draw_networkx_nodes(G, pos=nx.get_node_attributes(G, "pos"), nodelist=[node for node in range(dr.n1, dr.N)], node_color="g")
	nx.draw_networkx_labels(G, pos=nx.get_node_attributes(G, "pos"), font_color="w")
	width = 0.0
	for route in edges:
		width += 1
		nx.draw_networkx_edges(G, pos=nx.get_node_attributes(G, "pos"), edgelist=route, width=width, arrows=True)
	if sol == "Original":
		f.savefig("Network Graph of Original Solution.pdf")
	elif sol == "Swap":
		f.savefig("Network Graph of New Solution with Swap Function.pdf")
	elif sol == "Move":
		f.savefig("Network Graph of New Solution with 'Move Patient' function.pdf")

draw_solution(dr.solution, sol="Original")

solset = task2.solsearch(task2.swapfunction, dr.solution, 1000)
swapsol = solset[0]
costs = solset[1]

f = plt.figure()
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Change in cost over time with swap function")
plt.plot(range(1001), costs, linewidth=0.5)
f.savefig("Change in cost over time with swap function.pdf")

draw_solution(swapsol, sol="Swap")

solset = task2.solsearch(task2.movepatient, dr.solution, 1000)
movesol = solset[0]
costs = solset[1]

f = plt.figure()
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Change in cost over time with 'move patient' function")
plt.plot(range(1001), costs, linewidth=0.5)
f.savefig("Change in cost over time with 'move patient' function.pdf")

draw_solution(movesol, sol="Move")