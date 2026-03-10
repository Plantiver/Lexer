

class Exception:
    def __init__(self, details):
        self.det = details
    def __repr__(self):
        return f'Error: {self.det}'

class token:
    def __init__(self, value:str, priority):
        self.val = value
        self.prio = priority

    def __repr__(self):
        return f'{self.val}'

class char(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class num(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class space(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
    def __repr__(self):
        return " "
class colon(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class semicolon(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class oComp(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class cComp(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class oBra(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class cBra(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class equal(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class down(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class dot(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class oPar(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class cPar(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)
class bar(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)

class Other(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)


class word(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)


def goodToken(c:str):
    if c in [" ", "\t", "\n"]:
        return space(c, 0)
    elif c.isalpha():
        return char(c, 1)
    elif c.isdigit():
        return num(c, 2)
    elif c=="_":
        return down(c, 3)
    elif c=="<":
        return oComp(c,4)
    elif c=="{":
        return oBra(c,5)
    elif c=="|":
        return bar(c, 6)
    elif c=="=":
        return equal(c, 7)
    elif c==";":
        return semicolon(c, 8)
    
    ### And then, priority should be really high
    elif c==":":
        return colon(c, 100)
    elif c==">":
        return cComp(c, 100)
    elif c=="}":
        return cBra(c, 100)
    elif c==".":
        return dot(c, 100)
    return Other(c, 1000)



def step(tks:list[token]):
    ################## Look one by one for the less priority, and build it
    list_prio = [x.prio for x in tks]
    
    imin = list_prio.index(min(list_prio))

    if imin == len(list_prio)-1: return Exception("On est à bout")
    
    ## Check for two spaces
    if list_prio[imin] == 0 and list_prio[imin+1]==0:
        return tks[:imin] + [space()] + tks[imin+2:]



class tokenizer:
    def __init__(self, text:str):
        self.text = text
        self.tokenize()

    def tokenize(self):
        self.tokens = [goodToken(x) for x in list(self.text)]+[token("\0")]
        print(self.tokens)


        ############ From there, we just try to simplify it again and again #########

        self.cp = []
        while len(self.tokens)!=1 and self.tokens!=self.cp:
            self.cp = self.tokens[:]

            self.tokens = step(self.tokens)











def main():
    print("Hello world")
    t = tokenizer("""


Hey, how you doing?




""")


if __name__ == "__main__":
    main()
