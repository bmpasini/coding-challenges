import sys

class Solution(object):
    # find nodes that are not leaves
    # bfs -> max height is the height
    # put the min of these 'heights' in a set and return it
    
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents, tree = self.find_parent_nodes_and_form_tree(n, edges)
        min_height = sys.maxsize
        min_height_trees = list()
        for node in parents:
            height = self.find_height(tree, node)
            if height < min_height:
                min_height = height
                min_height_trees = [ node ]
            elif height == min_height:
                min_height_trees.append(node)
        return min_height_trees
        
    def find_height(self, tree, root):
        q = list()
        visited = set()
        q.append((root, 0))
        visited.add(root)
        max_height = 0
        while len(q) > 0:
            node, height = q.pop(0)
            max_height = max(height, max_height)
            for child in tree[node]:
                if child not in visited:
                    q.append((child, height+1))
                    visited.add(child)
        return max_height
    
    def find_parent_nodes_and_form_tree(self, n, edges):
        tree = [ set() for _ in range(n) ]
        for v, w in edges:
            tree[v].add(w)
            tree[w].add(v)
        parents = set()
        for i, edges in enumerate(tree):
            if len(edges) > 1:
                parents.add(i)
        return parents, tree

if __name__ == "__main__":
    s = Solution()
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(s.findMinHeightTrees(n, edges))
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    print(s.findMinHeightTrees(n, edges))


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        neighbors = collections.defaultdict(set)
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        pre_level, unvisited = [], set()
        for i in xrange(n):
            if len(neighbors[i]) == 1:  # A leaf.
                pre_level.append(i)
            unvisited.add(i)

        # A graph can have 2 MHTs at most.
        # BFS from the leaves until the number 
        # of the unvisited nodes is less than 3.
        while len(unvisited) > 2:
            cur_level = []
            for u in pre_level:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited: 
                        neighbors[v].remove(u)
                        if len(neighbors[v]) == 1:
                            cur_level.append(v)
            pre_level = cur_level
    
        return list(unvisited)











