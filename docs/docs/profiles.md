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
These documents can be found in this [dumps section](../dumps/loadout-ink).
Feel free to use these documents such that you find them helpful.

Below are how these object types will be *referred* to on this page. They are actualy stored as integers.

- `intIdHead`
- `intIdClothes`
- `intIdShoes`
- `intIdWeapon`
- `intIdAbility`

##### `Specification:`
- IDs passed must point to an object that exists.

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
### Ign
The IGN is simply stored as a string.

##### `Specification:`
- The string can not be longer than 10 characters.

### Sw
The SW is also stored as a string

##### `Specification`
- The string must consist entirely of digits.
- The string must be exactly 12 characters long.

### Ranks
Ranks are stored as either an integer or a float.
If the rank is stored as a float, it represents an X rank where the float represents the power.

If the rank is stored as an integer, it represents a standard rank.
The specific rank that integer represents is based on the [this data](../dumps/rank-powers/jp.json).

##### `Specification:`
- If the value stored is an integer, it must be one of the values present on the data.

### Level

Level is simply stored as an integer.
`*levels` are represented by any number above 99. `100` represents `*1`. `105` represents `*6`

##### `Specification:`
- The integer must be between 1 and 198.

### Weapon class
the `weapons.json` document is split into classes, each with their own id.
**Weapon** id's are only unique within the class, so the class id is also be stored.

##### `Specification:`
- Both the weapon id **and** class id must be passed.

### Sub abilities
Sub abilities are stored as an array of `IdAbility`s.
There is a maximum of 3 items in the array.

If there are less than 3 items in the array, missing items are blank.
An item as `null` represents an ability that isn't blank, but not yet unlocked.

For example: `[5, null]` represents 2 total sub abilities, with one of them unlocked with the id 5.

##### `Specification:`
- The length of the array must be between 1 and 3.
- All null values must appear after non-null values.
