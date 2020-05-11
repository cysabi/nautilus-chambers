from ariadne import ScalarType

rank_value = ScalarType("RankValue")

@rank_value.serializer
def serialize_rank(rank):
    return rank


@rank_value.value_parser
def parse_rank_value(rank):
    if "." in rank:
        return float(rank)
    return int(rank)


bindables = [rank_value]
