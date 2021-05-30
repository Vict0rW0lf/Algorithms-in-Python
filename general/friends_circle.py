#expected 2
friends = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

#expected 1
friendz = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Where N is the number of people
# Time(N ^ 2)
# Space(N)

def find_circles(matrix):
    visited = [False] * len(matrix)
    count = 0

    for person in range(len(matrix)):
        if visited[person]:
            continue

        dfs(matrix, visited, person)
        count += 1

    return count
        

def dfs(matrix, visited, i):
    visited[i] = True

    for j in range(len(matrix)):        
        if not visited[j] and  matrix[i][j] != 0:
            dfs(matrix, visited, j)


print(find_circles(friends))
print(find_circles(friendz))




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
'''
Time: O(N + M * log(N) where M is the number of edges we are given
and M is the number of nodes
we are only able to have this time complexity because we utilized
path compression here:
if self.parents[edge] != edge:
            self.parents[edge] = self.find(self.parents[edge])

without it it would be closer to O(N*M)
Space: O(N) where N is the number of nodes
'''

class DisjointSetUnion:
    circle_count = 0

    def __init__(self, size):
        parents = [None] * size
        
        for i in range(size):
            parents[i] = i

        self.parents = parents

    def union(self, edge1, edge2):
        parent1 = self.find(edge1)
        parent2 = self.find(edge2)

        self.parents[parent1] = parent2

    def find(self, edge):
        if self.parents[edge] != edge:
            self.parents[edge] = self.find(self.parents[edge])

        return self.parents[edge]
        
    def groups_count(self):
        unique = set()

        for i in range(len(self.parents)):
            unique.add(self.find(i))

        return len(unique)
        

def find_all_circles(matrix):
    DSU = DisjointSetUnion(len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                DSU.union(i, j)

    return DSU.groups_count()

print(find_all_circles(friends))
print(find_all_circles(friendz))
