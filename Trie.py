class TrieNode:
    def __init__(self):
        self.is_end = False
        self.neighbors = {}

    def add_node(self, letter):
        if letter in {'U', 'D', 'L', 'R', 'A', 'B'} and len(letter) == 1 and letter not in self.neighbors:
            self.neighbors[letter] = TrieNode()


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def build_trie(self, move_catalog):
        for move in move_catalog:
            self.add_move(move.strip())

    def add_move(self, move):
        curr = self.root
        for i in xrange(0,len(move)):
            char = move[i]
            if char not in curr.neighbors:
                curr.add_node(char)
            curr = curr.neighbors[char]
            if i == len(move) - 1:
                curr.is_end = True

    def dfs(self, root, so_far, moves):
        for key in root.neighbors.keys():
            if root.neighbors[key].is_end:
                moves.append(so_far+key)
            self.dfs(root.neighbors[key], so_far+key, moves)

    def get_moves(self, prefix):
        moves = []
        curr = self.root
        for i in xrange(0, len(prefix)):
            if prefix[i] in curr.neighbors:
                curr = curr.neighbors[prefix[i]]
            else:
                return moves
        self.dfs(curr, prefix, moves)

        return moves


def aux(input, idx, so_far, combos):
    for i in xrange(idx, len(input)):
        tmp = so_far+input[i]
        combos.append(tmp)
        aux(input, i + 1, tmp, combos)


def get_combos(input):
    combos = []
    aux(input, 0, '', combos)

    return combos


def get_moves(sub_move):
    to_return = set()
    combos = get_combos(sub_move)
    move_catalog = open('moveCatalog.txt','r')
    graph = Trie()
    graph.build_trie(move_catalog)
    for combo in combos:
        for res in graph.get_moves(combo):
            to_return.add(res)

    return to_return
            
    
print get_moves('RD')
