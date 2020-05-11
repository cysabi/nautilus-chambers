from .query import query_type
from .mutation import mutation_type
from .data import bindables as data
from .scalar import bindables as scalar


bindables = [query_type, mutation_type, *data, *scalar]
