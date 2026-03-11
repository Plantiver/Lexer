import tokenizer as tk
import Tree as tr

class Parser:
    def __init__(self, language:str):
        self.language = language
        self.tree = self.GenerateTree()
    
    def GenerateTree(self):
        tokenizer = tk.tokenizer(self.language)
        pseudoTree = tokenizer.parsedTree
        if pseudoTree is None: raise Exception("Bon, c'est pas très précis, mais il y a une erreur quelque part dans ton schéma")
        
        


def main():
    print("Hello world")

if __name__=="__main__":
    main()
