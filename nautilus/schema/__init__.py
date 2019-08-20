from ariadne import load_schema_from_path, make_executable_schema

from .abilities import abilities_type
from .wear import wear_type
from .rank import rank_type
from .gear import gear_type
from .meta import meta_type
from .status import status_type
from .profile import profile_type
from .query import query_type

bindables = [
    abilities_type, wear_type, rank_type, gear_type, meta_type, status_type,
    profile_type, query_type
]
