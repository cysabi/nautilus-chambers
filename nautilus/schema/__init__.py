from .query import query_type
from .mutation import mutation_type
from .data.wear import wearhead_type, wearclothes_type, wearshoes_type
from .data.abilities import abilities_type

bindables = [query_type, mutation_type, wearhead_type, wearclothes_type, wearshoes_type, abilities_type]
