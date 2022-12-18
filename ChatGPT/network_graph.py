import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import math

def import_from_excel(filename):
    # read excelfile into a dataframe
    df = pd.read_excel(filename)
    # initialize a dictionary for the connections
    connections = {}
    # create a dictionary from the dataframe
    for index, row in df.iterrows():
        node = row['node']
        connection = row['connection']
        weight = row['weight']
        if node not in connections:
            connections[node] = []
        connections[node].append({'node': connection, 'weight': weight})
    # return the dictionary
    return connections


def visualize_connections(connections, node_rgb_color):    
    G = nx.Graph()
    for node, connections in connections.items():
        G.add_node(node)
        for connection in connections:
            G.add_edge(node, connection['node'], weight=connection['weight'])
    # Use the spring layout to position the nodes
    # pos = nx.spring_layout(G, k=k, weight='weight', iterations=50, threshold=0.0001, scale=1, center=None, dim=2)
    k_factor = 5/(math.sqrt(len(G.edges)))
    pos = nx.fruchterman_reingold_layout(G, k=k_factor)
    print(f'len(G.edges)= {len(G.edges)}')
    # Set the node colors based on the rgb
    node_colors = [node_rgb_color for node in G.nodes()]
    # Set the edge colors based on the weight
    min_weight = min(G[u][v]['weight'] for u, v in G.edges())
    max_weight = max(G[u][v]['weight'] for u, v in G.edges())
    print(f'min_weight={min_weight}, max_weight={max_weight}')
    edge_colors = []
    for u, v in G.edges():
        weight = G[u][v]['weight']
        condition_big =  weight >= max_weight*0.8
        condition_medium = weight >= max_weight*0.2 and weight < max_weight*0.8 
        condition_small = weight > 0 and weight < max_weight*0.2
        color = (1, 1, 1) # default color white
        match weight:
            case _ if condition_big:
                color = (1, 0, 0) # red
            case _ if condition_medium:
                color = (0.3, 0.3, 0.3) # black
            case _ if condition_small:
                color = (0.8, 0.8, 0.8) # light grey
            case 0:
                color = (1, 1, 1) # white
        edge_colors.append(color)

    # Set the edge widths based on the weight
    edge_widths = []
    for u, v in G.edges():
        weight = G[u][v]['weight']
        condition_big =  weight >= max_weight*0.8
        condition_medium = weight >= max_weight*0.2 and weight < max_weight*0.8 
        condition_small = weight > 0 and weight < max_weight*0.2
        width = (1, 1, 1) # default color white
        match weight:
            case _ if condition_big:
                width = 3 
            case _ if condition_medium:
                width = 2
            case _ if condition_small:
                width = 1 
            case 0:
                width = 0
        edge_widths.append(width)
    # Draw the graph

    ax = plt.gca()  
    nx.draw(G, pos, node_size=130, node_color=node_colors, edge_color=edge_colors, with_labels=True, width=edge_widths)
    # nx.draw(G, pos, node_color=node_colors, edge_color=edge_colors, with_labels=True, width=edge_widths)
    # nx.draw(G, pos, node_color=node_colors, edge_color=edge_colors, with_labels=True, width=edge_widths)
    # Add a title to the graph
    import datetime
    # Get the current date
    now = datetime.datetime.now()
    # Format the date as a string
    date_string = now.strftime("%Y-%m-%d")

    #ax.set_title(f'Network Graph (k={round(k_factor,2)})', fontsize=20)
    
   # plt.figure(figsize=(24,9))
    plt.title(f'Network graph (k={round(k_factor,2)})\n', fontsize=20)
    plt.suptitle(f'{date_string} PW', fontsize=15, y=0.94)
    plt.savefig(f'D:\\OneDrive\\Github Output\\Network Graph\\Network_graph_k={round(k_factor,2)}.png', dpi=300, bbox_inches='tight')
    plt.show()
    return k_factor


def export_to_excel(connections):
    data = []
    for node, connections in connections.items():
        for connection in connections:
            data.append({'node': node, 'connection': connection['node'], 'weight': connection['weight']})
    df = pd.DataFrame(data)
    df.to_excel('connections_output.xlsx', index=False)

# settings
# r+g=yellow, g+b=light blue, r+b=magenta, 
node_rgb_color = (0.7, 0.7, 0.7)

# run functions
connections = import_from_excel('connections_input.xlsx')
visualize_connections(connections, node_rgb_color)
export_to_excel(connections)