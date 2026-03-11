

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


class priorityDefinition(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 3)
class priorityDeliDefi(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 3)

class defi(token):
    def __init__(self, value):
        super().__init__(value, 4)
class deli(token):
    def __init__(self, value):
        super().__init__(value, 4)
class classicText(token):
    def __init__(self, value):
        super().__init__(value, 4)

class expression(token):
    def __init__(self, value):          # value = [def1, def2, def3]
        super().__init__(value, 5)

class expressions(token):
    def __init__(self, value):          # value = [exp1, exp2, exp3]
        super().__init__(value, 6)

class partialDefinition(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 7)
class partialDeliDefi(token):
    def __init__(self, value):          # value = (prio, tk)
        super().__init__(value, 7)

class definition(token):
    def __init__(self, value):          # value = (partialDef, exps)
        super().__init__(value, 8)
class delimiter(token):
    def __init__(self, value):          # value = (partialDef, exps)
        # And then, we want to build our delimiter maybe a little more
        define, futurDelimiter = value
        if len(futurDelimiter)!=1:
            return Exception("Hey, there's a problem with your delimiter")
        futurDelimiter = futurDelimiter[0]
        if len(futurDelimiter)!=2:
            return Exception("Hey, there's a problem with your delimiter")
        futurDelimiter = (openingDelimiter(futurDelimiter[0]), closingDelimiter(futurDelimiter[1]))
        super().__init__((define, futurDelimiter), 8)

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
class EOF(token):
    def __init__(self):
        super().__init__("\0", 100)


class openingDelimiter(token):
    def __init__(self, value):
        super().__init__(value, 1000)
class closingDelimiter(token):
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



def step(tks:list[token], prio:list[int], tp:list[type], pmin:int):
    ################## Look one by one for the less priority, and build it
    if not (pmin in prio):
        return tks, None
    im = prio.index(pmin)

    if tp[im]==EOF: # If we reach the end, immediatly return
        return tks, None
    
    ## Check for priority 0
    if tp[im]==oComp:
        if tp[im+1] in [colon]:
            return tks[:im] + [defio(tks[im]+tks[im+1])] + tks[im+2:], None
        if tp[im+1] in [down]:
            return tks[:im] + [delio(tks[im]+tks[im+1])] + tks[im+2:], None
    if tp[im]==oBra:
        if tp[im+1] in [colon]:
            return tks[:im] + [absoo(tks[im]+tks[im+1])] + tks[im+2:], None
    if tp[im]==colon:
        if tp[im+1] in [cComp]:
            return tks[:im] + [defic(tks[im]+tks[im+1])] + tks[im+2:], None
        if tp[im+1] in [cBra]:
            return tks[:im] + [absoc(tks[im]+tks[im+1])] + tks[im+2:], None
        if tp[im+1] in [equal]:
            return tks[:im] + [assign(tks[im]+tks[im+1])] + tks[im+2:], None
    if tp[im]==down:
        if tp[im+1] in [cComp]:
            return tks[:im] + [delic(tks[im]+tks[im+1])] + tks[im+2:], None
    
    
    ## Check for priority 1
    if tp[im] in [defio, delio, absoo]:
        list_type = [type(x) for x in tks]
        if tp[im] == defio:
            if not (defic in list_type[im:]): return tks, Exception(f"Couldn't have find closing for {defio} delimiter")
            imax = list_type.index(defic, im)
            return tks[:im] + [defi("".join([x.val for x in tks[im:imax+1]]))] + tks[imax+1:], None
        if tp[im] == delio:
            if not (delic in list_type[im:]): return tks, Exception(f"Couldn't have find closing for {delio} delimiter")
            imax = list_type.index(delic, im)
            return tks[:im] + [deli("".join([x.val for x in tks[im:imax+1]]))] + tks[imax+1:], None
        if tp[im] == absoo:
            if not (absoc in list_type[im:]): return tks, Exception(f"Couldn't have find closing for {absoo} delimiter")
            imax = list_type.index(absoc, im)
            return tks[:im] + [classicText("".join([x.val for x in tks[im:imax+1]]))] + tks[imax+1:], None
    
    ## Check for priority 2
    if tp[im]==space:
        if tp[im+1] in [space]:
            return tks[:im] + [space(tks[im]+tks[im+1])] + tks[im+2:], None
    if tp[im]==num:
        if tp[im+1] in [num,down]:
            return tks[:im] + [num(tks[im]+tks[im+1])] + tks[im+2:], None
        if tp[im+1]==defi:
            return tks[:im] + [priorityDefinition((tks[im].val,tks[im+1].val))] + tks[im+2:], None
        if tp[im+1]==deli:
            return tks[:im] + [priorityDeliDefi((tks[im].val,tks[im+1].val))] + tks[im+2:], None
    # And with spaces
    if tp[im]==num and tp[im+1] == space:
        if tp[im+2]==defi:
            return tks[:im] + [priorityDefinition((tks[im].val,tks[im+2].val))] + tks[im+3:], None
        if tp[im+2]==deli:
            return tks[:im] + [priorityDeliDefi((tks[im].val,tks[im+2].val))] + tks[im+3:], None
    
    ## Check for priority 3
    if tp[im] == priorityDefinition and tp[im+1]==assign:
        return tks[:im] + [partialDefinition(tks[im].val)] + tks[im+2:], None
    if tp[im] == priorityDeliDefi and tp[im+1]==assign:
        return tks[:im] + [partialDeliDefi(tks[im].val)] + tks[im+2:], None
    # And with spaces
    if tp[im] == priorityDefinition and tp[im+1] == space and tp[im+2]==assign:
        return tks[:im] + [partialDefinition(tks[im].val)] + tks[im+3:], None
    if tp[im] == priorityDeliDefi and tp[im+1] == space and tp[im+2]==assign:
        return tks[:im] + [partialDeliDefi(tks[im].val)] + tks[im+3:], None
    
    ## Check for priority 4
    if tp[im] in [defi, deli, classicText]:
        return tks[:im] + [expression([tks[im].val])] + tks[im+1:], None
    
    ## Check for priority 5
    if tp[im] == expression and tp[im+1] == expression:
        return tks[:im] + [expression(tks[im].val+tks[im+1].val)] + tks[im+2:], None
    # And with spaces
    if tp[im] == expression and tp[im+1] == space and tp[im+2] == expression:
        return tks[:im] + [expression(tks[im].val+tks[im+2].val)] + tks[im+3:], None
    # If no way to make anything out of those expression, turn them to expressions, assuming that they won't combine anymore
    if tp[im] == expression:
        return tks[:im] + [expressions([tks[im].val])] + tks[im+1:], None
    
    ## Check for priority 6
    if tp[im] == expressions:
        if tp[im+1] == bar:
            if tp[im+2] == expressions:
                return tks[:im] + [expressions([tks[im].val+tks[im+2].val])] + tks[im+3:], None
            if tp[im+2] == space and tp[im+3]==expressions:
                return tks[:im] + [expressions([tks[im].val+tks[im+3].val])] + tks[im+4:], None
        if tp[im+1] == space and tp[im+2] == bar:
            if tp[im+3]==expressions:
                return tks[:im] + [expressions([tks[im].val+tks[im+3].val])] + tks[im+4:], None
            if tp[im+3]==space and tp[im+4] == expressions:
                return tks[:im] + [expressions([tks[im].val+tks[im+4].val])] + tks[im+5:], None

    ## Check for priority 7
    if tp[im] == partialDefinition:
        if tp[im+1] == expressions:
            return tks[:im] + [definition((tks[im].val, tks[im+1].val))] + tks[im+2:], None
        if tp[im+1] == space and tp[im+2] == expressions:
            return tks[:im] + [definition((tks[im].val, tks[im+2].val))] + tks[im+3:], None
    if tp[im] == partialDeliDefi:
        if tp[im+1] == expressions:
            return tks[:im] + [delimiter((tks[im].val, tks[im+1].val))] + tks[im+2:], None
        if tp[im+1] == space and tp[im+2] == expressions:
            return tks[:im] + [delimiter((tks[im].val, tks[im+2].val))] + tks[im+3:], None
    
    ## Check for priority 8:
    if tp[im]==definition:
        return tks[:im] + [definitions([tks[im].val])] + tks[im+1:], None
    if tp[im]==delimiter:
        return tks[:im] + [definitions([tks[im].val])] + tks[im+1:], None
    
    ## Check for priority 9:
    if tp[im]==definitions:
        if tp[im+1] == semicolon:
            if tp[im+2] == expressions:
                return tks[:im] + [definitions([tks[im].val+tks[im+2].val])] + tks[im+3:], None
            if tp[im+2] == space and tp[im+3]==definitions:
                return tks[:im] + [definitions([tks[im].val+tks[im+3].val])] + tks[im+4:], None
        if tp[im+1] == space and tp[im+2] == semicolon:
            if tp[im+3]==definitions:
                return tks[:im] + [definitions([tks[im].val+tks[im+3].val])] + tks[im+4:], None
            if tp[im+3]==space and tp[im+4] == definitions:
                return tks[:im] + [definitions([tks[im].val+tks[im+4].val])] + tks[im+5:], None
    
    
    
    # Maybe one extent, and we'll be fine
    if im == len(prio)-3: return tks, None
    
    
    res = step(tks[im+1:], prio[im+1:], tp[im+1:], pmin)
    return tks[:im+1]+res[0], res[1]


class tokenizer:
    def __init__(self, text:str):
        self.text = text
        self.parsedTree = None
        self.tokenize()

    def tokenize(self):
        verbose = False
        
        self.tokens = [goodToken(x) for x in list(self.text)]+10*[EOF()]  # The 10 others are for avoiding to check for some tokens out of reach
        if verbose: print(self.tokens)


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
        while len(self.cleanToken())!=1 and not finish:
            cp = []
            while self.tokens!=cp and not finish:
                cp = self.tokens[:]
                list_prio = [x.prio for x in self.tokens]
                list_type = [type(x) for x in self.tokens]
                pmin = min([x for x in list_prio if x>pm])
                
                if verbose:
                    print(pm)
                    print(self.tokens)
                    print(list_prio)
                    print(list_type)
                
                self.tokens, exc = step(self.tokens, list_prio, list_type, pmin)
                if exc: print(exc)
                finish = pmin==max(list_prio)
            pm = pmin
        if not finish:
            self.parsedTree = self.cleanToken()[0].val
        
    def cleanToken(self):
        return [x for x in self.tokens if not (type(x) in [space, EOF])]


def main():
    t = tokenizer("""
0<:del1o:> := {:/:};
0<:del1c:>:= {:\:};
1 <_del1_> := <:del1o:> <:del1c:>;
3<:del1c:> := {:Hello:}|{:World:};
3<:del1c:> := {:Does:}{:it:}{:work:}{:?:}
""")
    print(t.parsedTree)


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

