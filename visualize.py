import networkx as nx
import matplotlib.pyplot as plt
from models import get_connections, get_user_name

def visualize_graph():
    connections = get_connections()
    G = nx.Graph()

    for u, v in connections:
        G.add_edge(get_user_name(u), get_user_name(v))

    plt.figure()
    nx.draw(G, with_labels=True)
    plt.title("Relationship Network Graph")
    plt.show()