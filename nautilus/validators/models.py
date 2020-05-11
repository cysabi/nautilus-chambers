import re
from typing import List, Optional

from pydantic import BaseModel, validator

from nautilus.utils.object_data import get_object_by_id, get_rank
from .errors import InvalidID


class AbilitiesInput(BaseModel):
    main: int = None
    subs: List[Optional[int]] = None

    @validator('main')
    def v_main(cls, v):
        if v is None:
            return v
        if not (ability := get_object_by_id('abilities', v)):
            raise InvalidID(obj='abilities', id=v)
        return v
    
    @validator('subs')
    def v_subs(cls, v):
        if v is None:
            return v
        if len(v) > 3:
            raise TypeError('Sub-abilities array has more than 3 items.')
        # if (non-None appears after None):
        #     raise TypeError('Unlocked sub-abilities appear after locked ones.')
        for sub in v:
            if sub is not None:
                if not (ability := get_object_by_id('abilities', sub)):
                    raise InvalidID(obj='abilities', id=sub)
                if exclusive := ability.get('exclusive'):
                    raise TypeError(f'Ability is exclusive. ({exclusive})')
        return v


class HeadInput(BaseModel):
    id: int = None
    abilities: AbilitiesInput = None

    @validator('id')
    def v_id(cls, v):
        if v is None:
            return v
        if not get_object_by_id('head', v):
            raise InvalidID(obj='head', id=v)
        return v


class ClothesInput(BaseModel):
    id: int = None
    abilities: AbilitiesInput = None

    @validator('id')
    def v_id(cls, v):
        if v is None:
            return v
        if not get_object_by_id('clothes', v):
            raise InvalidID(obj='clothes', id=v)
        return v


class ShoesInput(BaseModel):
    id: int = None
    abilities: AbilitiesInput = None

    @validator('id')
    def v_id(cls, v):
        if v is None:
            return v
        if not get_object_by_id('shoes', v):
            raise InvalidID(obj='shoes', id=v)
        return v


class GearInput(BaseModel):
    weapon: dict = None
    head: HeadInput = None
    clothes: ClothesInput = None
    shoes: ShoesInput = None

    @validator('weapon')
    def v_weapon(cls, v):
        if v is None:
            return v
        if not get_object_by_id('weapons', v['class'], v['id']):
            raise InvalidID(obj='weapons', id=v)
        return v


def v_rank(v):
    if v is None:
        return v
    if not get_rank(value=v):
        raise ValueError('Rank must be one of the possible powers.')
    return v


class RankInput(BaseModel):
    sz: int = None
    rm: int = None
    tc: int = None
    cb: int = None
    sr: int = None

    v_sz = validator('sz', allow_reuse=True)(v_rank)
    v_rm = validator('rm', allow_reuse=True)(v_rank)
    v_tc = validator('tc', allow_reuse=True)(v_rank)
    v_cb = validator('cb', allow_reuse=True)(v_rank)
    v_sr = validator('sr', allow_reuse=True)(v_rank)


class StatusInput(BaseModel):
    ign: str = None
    sw: str = None
    level: int = None
    rank: RankInput = None
    gear: GearInput = None

    @validator('ign')
    def v_ign(cls, v):
        if v is None:
            return
        if not 1 <= len(v) <= 10:
            raise ValueError('IGN must be between 1 and 10 characters long.')

    @validator('sw')
    def v_sw(cls, v):
        if v is None:
            return v
        value = re.sub(r"[\D]", "", v)
        if len(value) != 12:
            raise ValueError('SW must be exactly 12 digits long.')
        return value

    @validator('level')
    def v_level(cls, v):
        if v is None:
            return v
        if not 1 <= v <= 198:
            raise ValueError('Level must be between 1 and *99 (198).')
        return v


class MetaInput(BaseModel):
    private: bool = None


class ProfileInput(BaseModel):
    meta: MetaInput = None
    status: StatusInput = None
