import functools
import itertools
from typing import AbstractSet as ASet, Tuple, Union, FrozenSet, collection
from collections import deque

from causality.utils import pairs_to_dict, union, visitte_deque

strint = Union[str, int]




class DAG:
    def __init__(self,
                 vertices: Collection[str],
                 edges: Collection[Tuple[str, str]]):
        self.vs = frozenset(vertices)
        self.edges = frozenset(edges)
        self._ch = pairs_to_dict(self.edges)
        self._pa = pairs_to_dict(self.edges, is_reversed=True)

        self.__an = functools.lru_cache()(self.an)
        self.__de = functools.lru_cache()(self.de)

        return False


    def subgraph(self, V_or_Vs, edge):
        if V_or_Vs in self.Vs and edge in self.edges:
            return V_or_Vs, edge
