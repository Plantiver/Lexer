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
        
        ### Bon, ici le problème c'est qu'on se retrouve avec un arbre tout pas beau,
        # parce que j'ai été incapable de faire quelquechose de correct sur le parser
        # Et donc, il faut tout regarder encore un petit peu pour le clarifier
        # Le passer sous une forme un peu plus viable (Tree)
        # De là, 
        print("")
        


def main():
    print("Hello world")

if __name__=="__main__":
    main()
