class FrozenList(list):
    _forbidden = {
        'insert', 'remove', 'pop', 'clear', 'sort', 'reverse', 
        '__setitem__', '__delitem__', '__iadd__', '__imul__'
    }

    def __getattribute__(self, item):
        if item in FrozenList._forbidden:
            raise AttributeError(f"FrozenList does not support {item}()")
        return super().__getattribute__(item)
