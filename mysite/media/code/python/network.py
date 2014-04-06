'''
Created on Apr 22, 2013

@author: zengxiaohan
@summary: A simple Python script to plot the social network in HBO's Game of Thrones,
          adapted from George R.R. Martin's A Song of Ice and Fire

@requires: numpy, networkx, matplotlib, community.py
@contact: zengxiaohanzxh@gmail.com
'''

from numpy import sqrt
import networkx as nx
import matplotlib.pyplot as plt
# from PyGrace.plot import PyGracePlot as pgp
import community
import json

def get_deg_dist(g):
    '''
    @summary: Function for plotting the degree distribution of the network
    @param g: The network
    @return: None
    '''
    degrees = g.degree(g.nodes())
    num_nodes = len(g.nodes())
    deg_dist, cum_deg_dist = {}, {}
    for deg in degrees.values():
        if not deg in deg_dist:
            deg_dist[deg] = 0
        deg_dist[deg] += 1
    degs = deg_dist.keys()
    degs.sort()
    for deg in degs:
        smaller = num_nodes
        for deg2 in degs:
            if deg2 < deg:
                smaller -= deg_dist[deg2]
        cum_deg_dist[deg] = smaller * 1. / num_nodes
    
    plot = pgp()
    plot.add_scattered(cum_deg_dist.items())
    plot.plot_fig('../asif.agr')
    
if __name__ == '__main__':
    edges = []
    houses = ['Stark', 'Tully', 'Baratheon', 'Targaryen',
              'Lannister', 'Greyjoy', 'Tarly', 'Tyrell','Arryn']
    for line in open('../data/asif.dat').readlines():
        line = line.strip('\n').strip(' ')
        name1, name2 = line.split('\t')
        edges.append([name1.strip(), name2.strip()])
    
    # Create the networkx instance
    g = nx.Graph()
    g.add_edges_from(edges)
    # Generate the graph layout
    pos = nx.graphviz_layout(g, prog='neato')
    degs = g.degree(g.nodes()).values()

    # Compute the network partition
    partition = community.best_partition(g)
    plt.figure(figsize=(20, 20))
    size = float(len(set(partition.values())))
    nw_json = {}
    nodes = sorted(g.nodes(), key=lambda n:g.degree(n), reverse=True)
    
    with open('/home/zxh/Works/Asoiaf_Wiki/items.json') as f:
        wiki_json = json.load(f)
    
    char_desc = {}
    for char in wiki_json:
        char_desc[char['name']] = char['description']
    
    nw_json["nodes"] = []
    for node in nodes:
        name_parts = node.split(' ')
        if len(name_parts) == 1:
            name = node
            house = ''
        elif len(name_parts) == 2:
            if name_parts[1] in houses:
                name = name_parts[0]
                house = name_parts[1]
            else:
                name = node
                house = ''
        else:
            name = node
            house = ''
        if node in char_desc:
            desc = char_desc[node]
        else:
            desc = ''
        nw_json["nodes"].append({"name":name,
                                 "group":partition[node],
                                 "degree":g.degree(node),
                                 "house":house,
                                 "desc":desc})
    
    nw_json["links"] = [{"source":nodes.index(edge[0]),
                         "target":nodes.index(edge[1])} 
                        for edge in g.edges()]
    with open('../data/a-song-of-ice-and-fire-desc.json', 'w') as out_file:
        json.dump(nw_json, out_file)
    exit()
    
    # Colors from colorbrewer2.org
    part_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3',
                   '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999']
    count = 0
    for com in set(partition.values()) :
        list_nodes = [nodes for nodes in partition.keys()
                                    if partition[nodes] == com]
        sizes = []
        for node in list_nodes:
            sizes.append(200 * sqrt(g.degree(node)))
        nx.draw_networkx_nodes(g, pos, list_nodes, node_size=sizes,
                               node_color=part_colors[count], alpha=1, linewidths=0)
        count = count + 1
    
    nx.draw_networkx_edges(g, pos, edge_color='grey', alpha=0.8)
    nx.draw_networkx_labels(g, pos, font_size=10, font_family='helvetica')
    plt.axis('off')
#     plt.savefig('../figures/asif_new.jpeg', dpi=300)
#     plt.show()
    
