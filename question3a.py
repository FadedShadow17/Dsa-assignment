class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def friend_requests(n, restrictions, requests):
    uf = UnionFind(n)
    result = []

    for req in requests:
        a, b = req

        rootA = uf.find(a)
        rootB = uf.find(b)

        can_be_friends = True

        for r1, r2 in restrictions:
            rootR1 = uf.find(r1)
            rootR2 = uf.find(r2)
            if (rootA == rootR1 and rootB == rootR2) or (rootA == rootR2 and rootB == rootR1):
                can_be_friends = False
                break

        if can_be_friends:
            uf.union(a, b)
            result.append("approved")
        else:
            result.append("denied")

    return result

n = 3
restrictions = [[0, 1]]
requests = [[0, 2], [2, 1]]
print(friend_requests(n, restrictions, requests))  

n = 5
restrictions = [[0, 1], [1, 2], [2, 3]]
requests = [[0, 4], [1, 2], [3, 1], [3, 4]]
print(friend_requests(n, restrictions, requests)) 
