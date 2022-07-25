# Tries / Prefix Trees / Digital Tree
# Ideal para lidar com strings. Cada nó contêm dicionários, cujas chaves são letras e seus valores são os próximos nós


class TrieNode:
    def __init__(self) -> None:
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word:str):
        current_node = self.root

        for char in word:
            # Se char estiver presente no dicionário do TrieNode atual
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        
        return current_node

    def insert(self, word):
        current_node = self.root

        for char in word:
            # Se o char já estiver presente, apenas avance para o próximo char
            if current_node.children.get(char):
                current_node = current_node.children[char]
            # caso contrário, crie uma nova chave para aquela letra
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node
        
        current_node.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):
        # node pode ser None
        current_node = node or self.root

        # key é um char, childNode é um TrieNode
        for key, childNode in current_node.children.items():
            if key == "*": # significa que chegamos ao final de uma palavra
                words.append(word)
            else: # significa que estamos no meio de uma palavra
                self.collectAllWords(childNode, word + key, words)
        return words
    
    def autocomplete(self, prefix):
        current_node = self.search(prefix)

        # Se essa palavra não for possível no Trie atual:
        if not current_node:
            return None
        return self.collectAllWords(current_node, "", [])
        # algo curioso: se não colocassemos os argumentos "" e [] acima, o método collectAllWords iria criar um atributo lista
        # inerente ao objeto. Então sempre que fossemos chamar meu_trie.autocomplete, ele iria sempre aumentar uma mesma lista na memória

    # Q4
    def autocorrect(self, word):
        current_node = self.root
        partial_word = ""
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
                partial_word += char
            else:
                possible_suggestions = []
                for rest in self.autocomplete(partial_word):
                    possible_suggestions.append(partial_word + rest)
                return possible_suggestions



        
meu_trie = Trie()

# EXERCISES
# Q1: word_list
word_list = ["tag", "tan", "tank", "tap", "today", "total"]
for word in word_list:
    meu_trie.insert(word)

# meu_trie.autocomplete("ta") # ['g', 'n', 'nk', 'p']

# Q3
def traverse_and_print(node: Trie):
    current_node = node.root
    def auxiliar(trie_node:TrieNode):
        if trie_node == None:
            return
        for char in trie_node.children.keys():
            print(char)
        for trienode in trie_node.children.values():
            auxiliar(trienode)
    return auxiliar(trie_node=current_node)

traverse_and_print(meu_trie)

# Q4: método definido na classe

for word in ["cat", "catnap", "catnip"]:
    meu_trie.insert(word)

print(meu_trie.autocorrect("catnar"))
print(meu_trie.autocorrect("caxasfdij"))