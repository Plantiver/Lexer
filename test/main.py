

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
    def __add__(self, tk):
        return self.val+tk.val


### Another way that I could try
"""
class tree:
    def __init__(self, v:str="", sub:list=[], prio=1000):
        self.v = v
        self.sub = sub
        self.prio = prio
    def __repr__(self):
        return f'({self.v}, {" ".join([str(x) for x in self.sub])})'

class space(tree):
    def __init__(self, v, sub:list=[]):
        super().__init__(v, prio=1)
    
    def __add__(self, other):
        if type(other)==space:
            return space(self.v+other.v, [self, other])
        return [self, other]
"""


class oComp(token):
    def __init__(self, value):
        super().__init__(value, 0)
class oBra(token):
    def __init__(self, value):
        super().__init__(value, 0)
class down(token):
    def __init__(self, value):
        super().__init__(value, 0)
class colon(token):
    def __init__(self, value):
        super().__init__(value, 0)

class defio(token):
    def __init__(self, value):
        super().__init__(value, 1)
class delio(token):
    def __init__(self, value):
        super().__init__(value, 1)
class absoo(token):
    def __init__(self, value):
        super().__init__(value, 1)

class space(token):
    def __init__(self, value):
        super().__init__(value, 2)
    def __repr__(self):
        return " "
class num(token):
    def __init__(self, value):
        super().__init__(value, 2)


class defi(token):
    def __init__(self, value):
        super().__init__(value, 3)
class deli(token):
    def __init__(self, value):
        super().__init__(value, 3)
        
class priorityDefinition(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 4)
class priorityDeliDefi(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 4)


class partialDefinition(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 4+1)
class partialDeliDefi(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 4+1)

class expression(token):
    def __init__(self, value):          # value = [def1, def2, def3]
        super().__init__(value, 5+1)

class expressions(token):
    def __init__(self, value):          # value = [exp1, exp2, exp3]
        super().__init__(value, 6+1)

class definition(token):
    def __init__(self, value):          # value = (partialDef, exps)
        super().__init__(value, 7+1)
class delimiter(token):
    def __init__(self, value):          # value = (partialDef, exps)
        super().__init__(value, 7+1)

class definitions(token):
    def __init__(self, value):         # value = [def1, def2, def3]
        super().__init__(value, 8+1)

class bar(token):
    def __init__(self, value):
        super().__init__(value, 100)
class semicolon(token):
    def __init__(self, value):
        super().__init__(value, 100)
class assign(token):
    def __init__(self, value):
        super().__init__(value, 100)
class equal(token):
    def __init__(self, value):
        super().__init__(value, 100)
class defic(token):
    def __init__(self, value):
        super().__init__(value, 100)
class delic(token):
    def __init__(self, value):
        super().__init__(value, 100)
class absoc(token):
    def __init__(self, value):
        super().__init__(value, 100)
class cComp(token):
    def __init__(self, value):
        super().__init__(value, 100)
class cBra(token):
    def __init__(self, value):
        super().__init__(value, 100)

class Other(token):
    def __init__(self, value):
        super().__init__(value, 100)


class openingDelimiter(token):
    def __init__(self, value):
        super().__init__(value, 1000)
class closingDelimiter(token):
    def __init__(self, value):
        super().__init__(value, 1000)
class classicText(token):
    def __init__(self, value):
        super().__init__(value, 1000)


class word(token):
    def __init__(self, value, priority):
        super().__init__(value, priority)


def goodToken(c:str):
    if c in [" ", "\t", "\n"]:
        return space(c)
    elif c.isdigit():
        return num(c)
    elif c=="_":
        return down(c)
    elif c=="<":
        return oComp(c)
    elif c=="{":
        return oBra(c)
    elif c=="|":
        return bar(c)
    elif c=="=":
        return equal(c)
    elif c==";":
        return semicolon(c)
    elif c==":":
        return colon(c)
    elif c==">":
        return cComp(c)
    elif c=="}":
        return cBra(c)
    return Other(c)



def step(tks:list[token], prio:list[int], pmin:int):
    ################## Look one by one for the less priority, and build it
    if not (pmin in prio):
        return tks, None
    imin = prio.index(pmin)

    # For now, we only need the actual character and the next one
    if imin == len(prio)-1: return tks, None
    
    
    ## Check for priority 0
    if type(tks[imin])==oComp:
        if type(tks[imin+1]) in [colon]:
            return tks[:imin] + [defio(tks[imin]+tks[imin+1])] + tks[imin+2:], None
        if type(tks[imin+1]) in [down]:
            return tks[:imin] + [delio(tks[imin]+tks[imin+1])] + tks[imin+2:], None
    if type(tks[imin])==oBra:
        if type(tks[imin+1]) in [colon]:
            return tks[:imin] + [absoo(tks[imin]+tks[imin+1])] + tks[imin+2:], None
    if type(tks[imin])==colon:
        if type(tks[imin+1]) in [cComp]:
            return tks[:imin] + [defic(tks[imin]+tks[imin+1])] + tks[imin+2:], None
        if type(tks[imin+1]) in [cBra]:
            return tks[:imin] + [absoc(tks[imin]+tks[imin+1])] + tks[imin+2:], None
        if type(tks[imin+1]) in [equal]:
            return tks[:imin] + [assign(tks[imin]+tks[imin+1])] + tks[imin+2:], None
    if type(tks[imin])==down:
        if type(tks[imin+1]) in [cComp]:
            return tks[:imin] + [delic(tks[imin]+tks[imin+1])] + tks[imin+2:], None
    
    
    ## Check for priority 1
    if type(tks[imin]) in [defio, delio, absoo]:
        list_type = [type(x) for x in tks]
        if type(tks[imin]) == defio:
            if not (defic in list_type[imin:]): return tks, Exception(f"Couldn't have find closing for {defio} delimiter")
            imax = list_type.index(defic, imin)
            return tks[:imin] + [defi("".join([x.val for x in tks[imin:imax+1]]))] + tks[imax+1:], None
        if type(tks[imin]) == delio:
            if not (delic in list_type[imin:]): return tks, Exception(f"Couldn't have find closing for {delio} delimiter")
            imax = list_type.index(delic, imin)
            return tks[:imin] + [deli("".join([x.val for x in tks[imin:imax+1]]))] + tks[imax+1:], None
        if type(tks[imin]) == absoo:
            if not (absoc in list_type[imin:]): return tks, Exception(f"Couldn't have find closing for {absoo} delimiter")
            imax = list_type.index(absoc, imin)
            return tks[:imin] + [classicText("".join([x.val for x in tks[imin:imax+1]]))] + tks[imax+1:], None
    
    ## Check for priority 2
    if type(tks[imin])==space:
        if type(tks[imin+1]) in [space]:
            return tks[:imin] + [space(tks[imin]+tks[imin+1])] + tks[imin+2:], None
    if type(tks[imin])==num:
        if type(tks[imin+1]) in [num,down]:
            return tks[:imin] + [num(tks[imin]+tks[imin+1])] + tks[imin+2:], None
        if type(tks[imin+1])==defi:
            return tks[:imin] + [priorityDefinition((tks[imin].val,tks[imin+1].val))] + tks[imin+2:], None
        if type(tks[imin+1])==deli:
            return tks[:imin] + [priorityDeliDefi((tks[imin].val,tks[imin+1].val))] + tks[imin+2:], None
    
    ## Check for priority 3
    if type(tks[imin]) == priorityDefinition and type(tks[imin+1])==assign:
        return tks[:imin] + [partialDefinition(tks[imin].val)] + tks[imin+2:], None
    if type(tks[imin]) == priorityDeliDefi and type(tks[imin+1])==assign:
        return tks[:imin] + [partialDeliDefi(tks[imin].val)] + tks[imin+2:], None
    
    ## Check for priority 4
    
    
    
    
    # We need to extend our reach by one
    if imin == len(prio)-2: return tks, None
    
    ## Check for priority 2
    if type(tks[imin])==num and type(tks[imin+1]) == space:
        if type(tks[imin+2])==defi:
            return tks[:imin] + [priorityDefinition((tks[imin].val,tks[imin+2].val))] + tks[imin+3:], None
        if type(tks[imin+2])==deli:
            return tks[:imin] + [priorityDeliDefi((tks[imin].val,tks[imin+2].val))] + tks[imin+3:], None
        
    ## Check for priority 3
    if type(tks[imin]) == priorityDefinition and type(tks[imin+1]) == space and type(tks[imin+2])==assign:
        return tks[:imin] + [partialDefinition(tks[imin].val)] + tks[imin+3:], None
    if type(tks[imin]) == priorityDeliDefi and type(tks[imin+1]) == space and type(tks[imin+2])==assign:
        return tks[:imin] + [partialDeliDefi(tks[imin].val)] + tks[imin+3:], None
    
    ## Check for priority 4
    
    
    # Maybe one extent, and we'll be fine
    if imin == len(prio)-3: return tks, None
    
    
    res = step(tks[imin+1:], prio[imin+1:], pmin)
    return tks[:imin+1]+res[0], res[1]


class tokenizer:
    def __init__(self, text:str):
        self.text = text
        self.tokenize()

    def tokenize(self):
        self.tokens = [goodToken(x) for x in list(self.text)]+[Other("\0")]
        print(self.tokens)


        ############ From there, we just try to simplify it again and again #########

        ## The way we're doing it:
        # find the highest priority (which here would be the lowest, but, yk)
        # Try to simplify things for this ranking, and if nothing can be done, increase the rank
        # Once something has been achieved, restart, with the lowest priority
        #
        # Do it again, until you reach max priority and can't do anything
        #
        # Okk, i've got things a little prettyer, and for now on, we don't need to go back and forth with pmin
        # Increasing it should be enough
        #
        

        finish = False
        pm=-1
        while len(self.tokens)!=1 and not finish:
            cp = []
            while self.tokens!=cp:
                cp = self.tokens[:]
                list_prio = [x.prio for x in self.tokens]
                pmin = min([x for x in list_prio if x>pm])
                
                print(pm)
                print(self.tokens)
                print(list_prio)
                
                self.tokens, exc = step(self.tokens, list_prio, pmin)
                if exc: print(exc)
            finish = pmin==max(list_prio)
            pm = pmin
        print(self.tokens)



def main():
    print("Hello world")
    t = tokenizer("""
0<:del1o:> := {:/:};
0<:del1c:>:= {:\:};
1 <_del1_> := <:del1o:> <:del1c:>;
3<:del1c:> := {:Hello:}|{:World:};
""")


if __name__ == "__main__":
    main()


"""

Okkk, dans l'idée, je voudrais que ça fasse:
 - delimiter avant et après et definitionSign
 - forme délimité
 - space et num et words (même s'il n'est pas censé y avoir de ces derniers)
 - priorityDefinition
 - partialDefinition
 - expression
 - expressions
 - Definition and DeliDefi
 - Definitions

"""

