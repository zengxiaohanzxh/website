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
#from PyGrace.plot import PyGracePlot as pgp
import community

#def get_deg_dist(g):
#    '''
#    @summary: Function for plotting the degree distribution of the network
#    @param g: The network
#    @return: None
#    '''
#    degrees = g.degree(g.nodes())
#    num_nodes = len(g.nodes())
#    deg_dist, cum_deg_dist = {}, {}
#    for deg in degrees.values():
#        if not deg in deg_dist:
#            deg_dist[deg] = 0
#        deg_dist[deg] += 1
#    degs = deg_dist.keys()
#    degs.sort()
#    for deg in degs:
#        smaller = num_nodes
#        for deg2 in degs:
#            if deg2 < deg:
#                smaller -= deg_dist[deg2]
#        cum_deg_dist[deg] = smaller * 1. / num_nodes
#    
#    plot = pgp()
#    plot.add_scattered(cum_deg_dist.items())
#    plot.plot_fig('../asif.agr')
    
if __name__ == '__main__':
    edges = []
    houses = ['Stark', 'Tully', 'Baratheon', 'Targaryen', 
              'Lannister', 'Theon', 'Tarly']
    for line in open('../data/asif.dat').readlines():
        line = line.strip('\n').strip(' ')
        name1, name2 = line.split('\t')
        if ' ' in name1:
            # Do not display names of houses
            if name1.split(' ')[1] in houses:
                name1 = name1.split(' ')[0]
        if ' ' in name2:
            if name2.split(' ')[1] in houses:
                name2 = name2.split(' ')[0]
        edges.append([name1, name2])
    
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
    
#    nx.draw_networkx_nodes(g, pos, node_size=sizes, node_color='r', linewidths=0)
    nx.draw_networkx_edges(g, pos, edge_color='grey', alpha=0.8)
    nx.draw_networkx_labels(g, pos, font_size=10, font_family='helvetica')
    plt.axis('off')
    plt.savefig('../figures/asif_new.jpeg', dpi=300)
#    plt.show()
    
