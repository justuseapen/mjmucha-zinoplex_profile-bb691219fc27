from django.db import models

# Create your models here.

class GraphNode(models.Model):
    links = models.ManyToManyField('self', symmetrical=False, through='graph_zinoplex.GraphLink')

    def outgoing_links(self):
        return GraphLink.objects.filter(source=self)

    def incoming_links(self):
        return GraphLink.objects.filter(target=self)

    def neighbor_nodes_undirected(self):
        targets = [link.target for link in self.outgoing_links()]
        sources = [link.source for link in self.incoming_links()]
        return list(set(targets+sources))

    def __str__(self):
        return 'Node'+str(self.pk)+'-'+self.profile.name()

class GraphLink(models.Model):
    source = models.ForeignKey(GraphNode, related_name='source')
    target = models.ForeignKey(GraphNode, related_name='target')

class GraphTreeNode(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True) # allow null because of root
    level = models.IntegerField()
    type = models.CharField(max_length='10') #root, community or person
    graph_node = models.ForeignKey(GraphNode, blank=True, null=True)

    def children(self):
        return self.objects.get(parent=self.pk)



# From: Python Patterns

# graph = {'A': ['B', 'C'],
#      'B': ['C', 'D'],
#      'C': ['D'],
#      'D': ['C'],
#      'E': ['F'],
#      'F': ['C']}

# Dijkstra's algorithm

def find_shortest_path(start:GraphNode, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    # if not graph.has_key(start):
    if len(start.neighbor_nodes_undirected()):
        return None
    shortest = None
    # for node in graph[start]:
    for node in start.neighbor_nodes_undirected():
        if node not in path:
            newpath = find_shortest_path(node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if len(start.neighbor_nodes_undirected()):
        return []
    paths = []
    for node in start.neighbor_nodes_undirected():
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths