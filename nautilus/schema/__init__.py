from .query import query_type
from .mutation import mutation_type
from .data.wear import wear_type
from .data.abilities import abilities_type

bindables = [query_type, mutation_type, wear_type, abilities_type]
