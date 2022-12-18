import pandas as pd

def prefill_excel(list_nodes):
    data = []
    for i, node1 in enumerate(list_nodes):
        for j, node2 in enumerate(list_nodes):
            if i < j:
                data.append({'node': node1, 'connection': node2, 'weight': 0})
    df = pd.DataFrame(data)
    df.to_excel('connections_input.xlsx', index=False)
    print("done in function")

list_nodes= ['Person A', 
    'Person B', 
    'Person C', 
    'Person D', 
    'Person E', 
    'Person F',
    'Person G',
    'Person H',
    'Person I',
    'Person J',
    'Person K']

prefill_excel(list_nodes)
print("done")  

