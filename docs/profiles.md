# Profiles

## How specific profile types are stored
> What represents what in the given context

### Splatoon 2 Objects
These types represent objects in Splatoon 2.
Information surrounding these objects remain completely constant, and therefore, do not need to be stored directly in the profiles.

Instead, an ID representing the object is stored in the database.
The IDs used are identical to the ones that can be found on [loadout.ink](https://github.com/selicia/selicia.github.io/tree/master/en_US/data)'s source catalog.

In practice, I have compiled each type [here](https://gist.github.com/LeptoFlare), modified for easy conversion.

Below are how these object types will be *referred* to on this page. They are stored as integers.

- `intIdHead`
- `intIdClothes`
- `intIdShoes`
- `intIdWeapon`
- `intIdAbility`

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

### Level

Level is simply stored as an integer.

`*levels` are represented by any number above 99. `100` represents `*1`. `105` represents `*6`

### Sub Abilities

Sub abilities are stored as an array containing `IdAbility`.

There should be a maximum of 3 items in the array.

If there are less than 3 items in the array, missing items are blank.

`null` values represent abilities that are not blank, but not yet unlocked.

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
            "sz": int,
            "tc": int,
            "rm": int,
            "cb": int,
            "sr": int
        },
        "gear": {
            "weapon": intIdWeapon,
            "head": {
                "id": intIdHead,
                "abilities": {"main": intIdAbility, "subs": [intIdAbility]}
            },
            "clothes": {
                "id": intIdClothes,
                "abilities": {"main": intIdAbility, "subs": [intIdAbility]}
            },
            "shoes": {
                "id": intIdShoes,
                "abilities": {"main": intIdAbility, "subs": [intIdAbility]}
            }
        }
    }
}
```
