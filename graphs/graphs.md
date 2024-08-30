## Graphs

Many applications require a collection of items and relationship between said items.

Examples of this can be seen in maps, where items are cities and connections are roads. Or the web, where items are pages and the connections are hyperlinks

Some collections you may be familiar with are:
- lists, a linear sequence of items
- trees, a branched hierachy of items

Graphs are more general and allow for abitrary connections

A graph G = (V, E)
- V is a set of vertices
- E is a set of edges

Nodes are distinguished by a unique indentifier.
Edges may be (optionally) directed, labelled and or weighed.

Graph algorithms are generally more complex than tree/list ones, this is because they have no implicit order of times. Graphs may contain cycles. A concrete representation is less obvious and an algorithm's complexity depends on connection complexity.

A graph with V vertices has at most V(V-1)/2 edges.

The ratio E:V can vary considerably.
- E is closer to V^2 when the graph is dense
- E is closer to V when the graph is sparse

Knowing whether or not a graph is sparse or dense is important, it may affect your choice of data structure to represent the graph and it also may affect the choice of algorithm to process the graph.

## Graph Terminology

For an edge that connects vertices v and w, v and w are adjacent (neighbours), e is incident on both v and w.

Degree of a vertex v is the number of edges incident on e.

Say edge v has 2 edges incoming/outgoing (incident), the degree of v is 2.

Synonyms:
- vertex = node
- edge = arc = link (arc is sometimes used for directed edges specifically)

A path is a sequence of vertices where each vertex has an edge to its predecessor.

A cycle is a path where the last vertex in the path is the same as the first vertex in the path.

Length of path or cycle = number of edges.

A connected graph is when there's a path from each vertex to every other vertex, if a graph is not connected, it has >=2 connected components.

A complete graph is when there is an edge from each vertex to every other vertex, in a complete graph E = V(V-1)/2

A tree is a connected (sub)graph with no cycles.

A spanning tree is a tree containing all vertices. A spanning tree of connected graph G = (V, E) is a subgraph of G containing all of V and is a single tree (connected, no cycles).

A clique is a complete subgraph.

A spanning forest of non-connected graph G = (V, E) is a subgraph of G containing all of V, and is a set of trees (not connected, no cycles), with one tree fo reach connected component.

You can form spanning trees from graphs by removing edges.

Undirected graph, edge(u, v) == edge(v, u), no self-loops (i.e. no edge(v, v)).
Directed graph, edge(u, v) != edge(v, u), can have self loops (i.e. edge(v, v)).

Some other types of graphs include:
- Weighted Graph, where each edge has an associated value (weight), e.g. a road map (weights on edges are distances between cities).
- Multi-Graphs, which allow edges between two vertices, e.g. function call graph (f() calls g() in several places).
- Labelled Graphs, edges have associated labels, this can be used to add semantic information.

## Graph Representations

There are 3 main graph representations

- Adjacency Matrix, edges defined by presence value in a V x V matrix
- Adjacency List, edges defined by entires in array of V lists
- Array of edges, explicit representation of edges as (v, w) pairs

We'll consider these representations for unweighted and directed graphs

# undirected
```
[
    0, 1, 0, 1
    1, 0, 0, 1
    0, 0, 0, 1
    1, 1, 1, 0
]
```

will give us a graph that looks like:
```
1 - 3 - 2
 \ /
  0
```

# directed
```
[
    0, 1, 0, 1
    1, 0, 0, 1
    0, 0, 0, 0
    0, 0, 1, 0
]
```

will give us a graph that looks like:
```
1 -> 3 -> 2
^   ^
 \ /
 v
  0
```

# Advantages 
- Efficient, edge insertion/deletion and adjaccency check is O(1)
# Disadvantages
- HUGE MEMORY USAGE O(V^2), sparse graphs waste space and undirected graphs waste space


