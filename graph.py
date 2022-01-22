import math
from vec2 import Vec2

NODE_RADIUS = 120

#------------------------------------------------------------------------------
# Representation for the full graph
class Graph():
    def __init__(self):
        self.nodes = []
        self.edges = []

class Edge():
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

#------------------------------------------------------------------------------
# View Model
class ViewModel():
    def __init__(self):
        self.nodes = []
        self.edges = []

class VisualNode():
    def __init__(self):
        self.pos = Vec2(0, 0)
        self.highlight = False
        pass

#------------------------------------------------------------------------------
# App state
class Game():
    def __init__(self, fullGraph):
        self.fullGraph = fullGraph
        self.currNode = fullGraph.nodes[0]

        self.afferent = dict()
        self.efferent = dict()
        for node in fullGraph.nodes:
            self.afferent[node] = []
            self.efferent[node] = []

        for edge in fullGraph.edges:
            self.afferent[edge.dst].append(edge.src)
            self.efferent[edge.src].append(edge.dst)

        self.k = 0

    def tick(self, userInput):
        viewModel = ViewModel()
        viewModel.edges = self.fullGraph.edges

        if userInput.click == True:
            self.k = (self.k + 1) % len(self.fullGraph.nodes)
        if userInput.click2 == True:
            self.k = (self.k - 1 + len(self.fullGraph.nodes)) % len(self.fullGraph.nodes)

        self.currNode = self.fullGraph.nodes[self.k]

        # layout nodes
        i = 0
        N = len(self.afferent[self.currNode])
        radius = NODE_RADIUS * 5
        for name in self.afferent[self.currNode]:
            if name == self.currNode:
                continue
            angleFraction = math.pi / (N + 2)
            angle = - ((1+i+0.5) * angleFraction)
            vnode = VisualNode()
            vnode.name = name
            vnode.pos = Vec2(math.cos(angle), math.sin(angle)) * radius
            viewModel.nodes.append(vnode)
            i += 1

        i = 0
        N = len(self.efferent[self.currNode])
        radius = NODE_RADIUS * 5
        for name in self.efferent[self.currNode]:
            if name == self.currNode:
                continue
            angleFraction = math.pi / (N + 2)
            angle = + ((1+i+0.5) * angleFraction)
            vnode = VisualNode()
            vnode.name = name
            vnode.pos = Vec2(math.cos(angle), math.sin(angle)) * radius
            viewModel.nodes.append(vnode)
            i += 1

        vnode = VisualNode()
        vnode.name = self.currNode
        vnode.pos = Vec2(0, 0)
        vnode.highlight = True
        
        viewModel.nodes.append(vnode)

        return viewModel



