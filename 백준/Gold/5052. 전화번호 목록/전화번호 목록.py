import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, has_end=False):
        self.has_end = has_end
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, num):
        curr_node = self.head
        for d in num:
            if curr_node.children.get(d) is None:
                curr_node.children[d] = Node()

            curr_node = curr_node.children[d]
        curr_node.has_end = True
    
    def search(self, num):
        curr_node = self.head

        for d in num:
            if curr_node.children.get(d) is None:
                return True
            curr_node = curr_node.children[d]
            if curr_node.has_end:
                return False
        return True
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        phone_numbers = [input().rstrip() for _ in range(n)]

        phone_numbers = list(map(lambda x: (len(x), x), phone_numbers))
        phone_numbers.sort(key = lambda x: x[0])

        data = Trie()
        for _, number in phone_numbers:
            if data.search(number) == False:
                print("NO")
                break
            data.insert(number)
        else:
            print("YES")
