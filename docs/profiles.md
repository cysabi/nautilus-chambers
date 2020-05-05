# Profiles

## How specific profile types are stored
> What represents what in the given context

### Splatoon 2 Objects
These types represent objects in Splatoon 2.
Information surrounding these objects remain completely constant, and therefore, do not need to be stored directly in the profiles.

Instead, an ID representing the object is stored in the database.
The IDs used are identical to the ones that can be found on [loadout.ink](https://github.com/selicia/selicia.github.io/tree/master/en_US/data)'s object data source.

When using the API, these IDs are to be sent when inserting or updating a profile.
However, when reading a profile, the actual object data from loadout.ink is returned.

#### Data sources
In order to help with parsing, json documents with the data on each object have been compiled.
Recognizing this may prove helpful to others as well, the documents have been seperated from nautilus.
These documents are located on a [Github Gist](https://gist.github.com/LeptoFlare/00bd27c4e27158bdc302ffccc2a91931).
Feel free to use these documents such that you find them helpful.

Below are how these object types will be *referred* to on this page. They are actualy stored as integers.

- `intIdHead`
- `intIdClothes`
- `intIdShoes`
- `intIdWeapon`
- `intIdAbility`

## Database profiles collection
> A complete profile template as how it is stored in the database, with types for each key.
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
            "weapon": {
                "id": intIdWeapon,
                "class": int,
            },
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

### Weapon class
the `weapons.json` document is split into classes, each with their own id.
Actual weapon id's are only unique within the class, so the class id must also be stored.

### Sub abilities
Sub abilities are stored as an array of `IdAbility`s.
There is a maximum of 3 items in the array.

If there are less than 3 items in the array, missing items are blank.

An item as `null` represents an ability that isn't blank, but not yet unlocked.


