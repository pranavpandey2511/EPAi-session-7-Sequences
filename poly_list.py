import math
import operator
from functools import reduce, lru_cache
from polygon import Polygon

class PolyList:
    def __init__(self, n_edges_max: int, circumradius: float):
        assert n_edges_max > 2, "Number of edges should atleast be 3."
        self._n_edges_max = n_edges_max
        self._circumradius = circumradius

    def __getitem__(self, index):
        if isinstance(index, int):
            # single item requested
            if index < 0:
                index = self._n_edges_max + index
            if index < 0 or index > self._n_edges_max - 1:
                raise IndexError
            return self._polygon(self,index)
        else:
            # slice is requested
            idx = index.indices(self._n_edges_max)
            rng = range(*idx)
            return [self._polygon(self,n) for n in rng]
    
    @property
    def most_efficient(self):
        """Most efficient polygon in terms of area:perimeter ratio.
        This will always be the max vertices polygon."""
        
        return Polygon(n_edges=self._n_edges_max, circumradius=self._circumradius)
        
        
    @staticmethod
    @lru_cache(2**10)        
    def _polygon(self, n_edges):
        if n_edges == 3 or n_edges == 2 or n_edges == 1 or n_edges == 0:
            return Polygon(n_edges=3, circumradius = self._circumradius)
        else:
            return Polygon(n_edges=n_edges, circumradius = self._circumradius)
            
        
    def __len__(self):
        return self._len_edges_max
    def __repr__(self):
        return "Custom polygon sequence"