Contains json documents with Splatoon 2 object data sourced from [loadout.ink](https://github.com/selicia/selicia.github.io/tree/master/en_US/data) for easy parsing.

Each json document represents all objects of a particular object type.

## Files
- [`abilities.json`](abilities.json)
- [`clothes.json`](clothes.json)
- [`head.json`](head.json)
- [`shoes.json`](shoes.json)
- [`specials.json`](specials.json)
- [`subs.json`](subs.json)
- [`weapons.json`](weapons.json)

## Changes from original source
- `weapons.json`:
  - The keys inside of `"stats"` have been converted to camelCase.
  - The weapon class key `"type"` has been renamed `"name"`
  - The weapon `"class"` key's value is now the id of the class.
  - Each of the the values in `minDamage`, `maxDamage`, and `mpuMaxDamage` that aren't maps have been casted into maps, under the key "damage".