# 790. Parser

**Description**

Symbol string generator consists of two parts, a set of the start symbol and a set of rules of generation.

For example:

```
Start symbol: ['S'], Rules of generation: ["S -> abc", "S -> aA", "A -> b", "A -> c"]
Then, symbolic string abc can be generated because S -> abc.
Symbolic string ab can be generated because S -> aA -> ab.
Symbolic string abc can be generated because S -> aA -> ac.
Now, give you a symbolic string generator and a symbolic string, and you need to return True if the symbolic string can be generated, False otherwise
```

```
You can assume the left side of the generation rule is an uppercase letter, startSymbol is an uppercase letter, symbolString is a lowercase string
|generator| <= 20, |symbolString| <= 20
There is no left recursion in generate rule sets. For example, there is no such rule set as ["S -> Sb", "S -> A", "A -> Sb"]
```

**Example**

```
Example 1:
	Input:  generator = ["S -> abc", "S -> aA", "A -> b", "A -> c"], startSymbol = S, symbolString = “ac”
	Output:  true
	
	Explanation:
	S -> aA -> ac

Example 2:
	Input: generator = ["S -> abcd", "S -> A", "A -> abc"], startSymbol = S, symbolString = “abc”
	Output:  true
	
	Explanation:
	S -> A -> abc
	
Example 3:
	Input: generator = ["S -> abc", "S -> aA", "A -> b", "A -> c"], startSymbol = S, symbolString = “a”
	Output:  false
	
	Explanation:
	Cannot get 'a' from S with several steps.
```


**DFS**


```python
class Solution:
    """
    @param generator: Generating set of rules.
    @param startSymbol: Start symbol.
    @param symbolString: Symbol string.
    @return: Return true if the symbol string can be generated, otherwise return false.
    """
    def canBeGenerated(self, generator, startSymbol, symbolString):
        # Write  your code here.
        if not generator or len(generator) == 0:
            return False

        if startSymbol == symbolString:
            return True

        sym = [[] for i in range(26)]
        for i in generator:
            sym[self.getIdx(i[0])].append(i[5:])

        idx = self.getIdx(startSymbol)
        for i in sym[idx]:
            if self.isMatched(symbolString, 0, i, sym):
                return True

        return False


    def getIdx(self, c):
        return ord(c) - ord('A')
        
        
    def nonTerminal(self, c):
        return ord(c) >= ord('A') and ord(c) <= ord('Z')
        
        
    def isMatched(self, s, pos, gen, sym):
        if pos == len(s):
            if len(gen) == 0:
                return True
            else:
                return False
        else:
            if len(gen) == 0:
                return False
            elif self.nonTerminal(gen[0]):
                idx = self.getIdx(gen[0])
                for i in sym[idx]:
                    if self.isMatched(s, pos, i + gen[1:], sym):
                        return True
            elif gen[0] == s[pos]:
                if self.isMatched(s, pos + 1, gen[1:], sym):
                    return True
            else:
                return False

        return False
```
