class Trie:
    def __init__(self):
        self.root = {"*" : "*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node["*"] = "*"

    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return "*" in curr_node
    
    def print_trie(self):
        curr_node = self.root
        for letter in curr_node:
            print(curr_node)
            print(curr_node[letter])
           # print(curr_node[letter])

            #for item in curr_node[letter]:
                #print(item)


trie = Trie()
words = ["pipe", "pipeline", "cup", "cupping"]
for word in words:
    trie.add_word(word)

print(trie.does_word_exist("pipe")) #True
print(trie.does_word_exist("hockey")) #False
print(trie.does_word_exist("cup"))
#trie.print_trie()







