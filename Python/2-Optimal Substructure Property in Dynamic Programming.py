# 2) Optimal Substructure: A given problems has Optimal Substructure Property 
# if optimal solution of the given problem can be obtained by using optimal 
# solutions of its subproblems.

# For example, the Shortest Path problem has following optimal substructure 
# property:
# If a node x lies in the shortest path from a source node u to destination 
# node v then the shortest path from u to v is combination of shortest path
# from u to x and shortest path from x to v. The standard All Pair Shortest
# Path algorithms like Floyd–Warshall and Bellman–Ford are typical examples 
# of Dynamic Programming.

# reference:https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/