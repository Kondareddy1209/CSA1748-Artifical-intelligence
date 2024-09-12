edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(c, g).

% Breadth-first search
bfs(Start, Goal) :- bfs_queue([[Start]], Goal).

bfs_queue([[Node|Path]|_], Node) :- reverse([Node|Path], Solution), write(Solution), nl.
bfs_queue([Path|Paths], Goal) :- extend(Path, NewPaths), append(Paths, NewPaths, Queue), bfs_queue(Queue, Goal).

extend([Node|Path], NewPaths) :- findall([NewNode, Node|Path], (edge(Node, NewNode), \+ member(NewNode, [Node|Path])), NewPaths).
