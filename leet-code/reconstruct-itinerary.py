import collections

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        g = collections.defaultdict(list)
        order = list()
        for f, t in tickets:
            g[str(f)].append(str(t))
        self.dfs(g, 'JFK', order)
        return order[::-1]
    
    def dfs(self, g, v, order):
        for adj in sorted(g[v]):
            if adj in g[v]:
                g[v].remove(adj)
                self.dfs(g, adj, order)
        order.append(v)