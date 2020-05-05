# Profiles

## How specific profile types are stored
> What represents what in the given context

### Splatoon 2 Objects
These types represent objects in Splatoon 2.
Information surrounding these objects remain completely constant, and therefore, do not need to be stored directly in the profiles.

Instead, an ID representing the object is stored in the database.
The IDs used are identical to the ones that can be found on [loadout.ink](https://github.com/selicia/selicia.github.io/tree/master/en_US/data)'s source catalog.
In practice, I have compiled each relavent type [here](https://gist.github.com/LeptoFlare) for easy translation.

Below are how these object types will be referred to on this page. They are stored as integers.

- `IdHead`
- `IdClothes`
- `IdShoes`
- `IdWeapon`
- `IdAbility`

### Ranks
Ranks are stored as either an integer or a float.
If the rank is stored as a float, it represents an X rank with the float representing the power.

If the rank is stored as an integer, it represents a standard rank as seen here:
> ```json
> {
>     "C-": 1000,
>     "C": 1100,
>     "C+": 1200,
>     "B-": 1250,
>     "B": 1450,
>     "B+": 1550,
>     "A-": 1650,
>     "A": 1700,
>     "A+": 1800,
>     "S": 1900,
>     "S+0": 2000,
>     "S+1": 2080,
>     "S+2": 2120,
>     "S+3": 2160,
>     "S+4": 2200,
>     "S+5": 2230,
>     "S+6": 2260,
>     "S+7": 2290,
>     "S+8": 2320,
>     "S+9": 2350
> }
> ```

The integer representations used are identical to the ones found [here](https://oatmealdome.me/blog/an-in-depth-look-at-the-splatoon-2-ranking-system/).

This object type will be referred to on this page as `IntRank`

## Database Collections
> The structure of the database and the relations between collections.

Relations between collections will be referred to on this page like this: `ObjectId(collection)`.
Where `ObjectId` represents the `bson.ObjectId` class, with `collection` representing a document ID from the named collection.

### `db.profiles`
> A complete profile template with the types of each key.
```json
{
    "meta": {
        "private": bool
    },
    "status": {
        "ign": str,
        "sw": str,
        "level": int,
        "rank": {
            "sz": IntRank,
            "tc": IntRank,
            "rm": IntRank,
            "cb": IntRank,
            "sr": IntRank,
        },
        "gear": {
            "weapon": IdWeapon,
            "head":    {"id": IdHead, "abilities": ObjectId(db.abilities)},
            "clothes": {"id": IdClothes, "abilities": ObjectId(db.abilities)},
            "shoes":   {"id": IdShoes, "abilities": ObjectId(db.abilities)}
        }
    }
}
```

### `db.abilities`
> Sub-profile collection containing an ability set.
```json
{
    "main": IdAbility,
    "subs": [IdAbility, IdAbility, IdAbility]
}
```
