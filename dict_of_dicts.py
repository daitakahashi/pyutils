
# assume that a dict keeps keys' order (i.e., python >= 3.7)
class DictOfDicts:
    def __init__(self, dict_of_dicts):
        self._dd = dict_of_dicts

    def values(self):
        def _values(x):
            for y in x.values():
                if isinstance(y, dict):
                    yield from _values(y)
                else:
                    yield y
        return _values(self._dd)

    def map(self, f):
        # self.map(f) == self.assimilate(f(x) for x in self.values())
        d = {}
        def _map(x, d):
            for k, y in x.items():
                if isinstance(y, dict):
                    d[k] = {}
                    _map(y, d[k])
                else:
                    d[k] = f(y)

        _map(self._dd, d)
        return d

    def assimilate(self, seq):
        seq_iter = iter(seq)
        return self.map(lambda x: next(seq_iter))

    def items(self):
        def _items(x, ks):
            for key, y in x.items():
                k = ks + (key,)
                if isinstance(y, dict):
                    yield from _items(y, k)
                else:
                    yield (k, y)
        return _items(self._dd, ())

    def keys(self):
        def _keys(x, ks):
            for key, y in x.items():
                k = ks + (key,)
                if isinstance(y, dict):
                    yield from _keys(y, k)
                else:
                    yield k
        return _keys(self._dd, ())

    def __iter__(self):
        return self.keys()

    def __getitem__(self, key):
        d = self._dd
        for k in key:
            d = d[k]
        return d
