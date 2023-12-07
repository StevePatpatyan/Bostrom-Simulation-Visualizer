from treelib import Tree, Node
from random import randint
from time import sleep

# create our tree and root node/base reality
tree = Tree()
tree.create_node("Base", "base")

# take user input that will serve as the number of child nodes/sims each node/reality has. If the user inputs something other than a whole number, number of sims will be a random number from 1 to 5
try:
    num_sims = int(input("Enter the number of simulations that we create: "))
except:
    print("Invalid input! Picking a random number from one to 5...")
    sleep(2)
    num_sims = randint(1, 5)

print(f"Number of simulations per reality is: {num_sims}")
sleep(2)

# take user input that will serve as the depth of the tree/how far downward it goes. If the user inputs something other than a whole number, depth will be a random number from 1 to 5
try:
    depth = int(input("Enter the depth of the diagram: "))
except:
    print("Invalid input! Picking a random number from one to 5...")
    sleep(2)
    depth = randint(1, 5)

print(f"Depth of simulation hypothesis visual: {depth}")
sleep(2)

print("Creating tree...")
sleep(1)
# create the simulation tree by inserting num_sims child nodes/sims into each node/reality. Stop at a tree depth of DEPTH to avoid infinite execution
simulationNum = 1
childlessNodes = list(tree.nodes.keys())
for x in range(depth):
    print(f"Layer {x+1} being created...")
    for node in childlessNodes:
        toBeChildlessNodes = []
        for sim in range(num_sims):
            toBeChildlessNodes.append(
                tree.create_node("Sim", f"sim {simulationNum}", parent=node).identifier
            )
            simulationNum += 1
        childlessNodes.remove(node)
    childlessNodes += toBeChildlessNodes
    print(f"Layer {x+1} complete.")

# make graphviz/dot representation of tree
print("Visualizing hypothesis...")
sleep(1)
tree.to_graphviz("visual.dot")

# create diagram of tree as png using graphviz/dot
import subprocess
import graphviz

subprocess.call(["dot", "-Tpng", "visual.dot", "-o", "graph.png"])
