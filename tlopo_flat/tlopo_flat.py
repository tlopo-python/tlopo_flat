class Flat:
    def __init__(self, separator=None):
        self.stack = []
        self.hashmap = {}
        self.separator = separator or " | "

    def to_dictionary(self, e):
        self.flat_rec(e)
        return self.hashmap

    def to_string(self, e):
        self.flat_rec(e)
        r = []
        for k,v in self.hashmap.items():
            r.append(f"{k} = {v}")
        return "\n".join(r)
    
    def pop(self,stack):
        if len(stack) > 0:
            stack.pop()

    def flat_rec(self,e, name=None, stack=None):
        if name == None:
            name = ""
        if stack == None:
            stack = []

        self.stack = stack
        
        if isinstance(e, dict) and len(e) > 0:
            for k in e.keys():
                self.stack.append(k)
                self.flat_rec(e[k], k, self.stack)
            self.pop(stack)

        elif isinstance(e, list) and len(e) > 0:
            for index, item in enumerate(e):
                self.stack.append(str(index))
                self.flat_rec(item, index, self.stack)
            self.pop(stack)
            
        else:
            self.hashmap[self.separator.join(self.stack)] = e
            self.pop(stack)
            return
