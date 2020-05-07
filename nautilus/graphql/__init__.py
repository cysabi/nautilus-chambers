from .query import query_type
from .mutation import mutation_type
from .data import __all__


bindables = [query_type, mutation_type, *__all__]
