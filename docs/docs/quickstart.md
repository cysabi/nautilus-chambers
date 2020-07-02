# Quickstart

### 1. Navigate to the [API endpoint](usage) to check if the graphql playground is working.
  ![GraphQL Playground](playground.png)

### 2. Get an [authorization token](auth).

### 3. Open up the playground and add your Authorization header in the `HTTP HEADERS` section at the bottom of the page.
  > ```json
  > {
  >     "Authorization": "Bearer eyJhb...XVCJ9"
  > }
  > ```

### 4. In the main area and enter this:
  > ```gql
  > query {
  >   readProfile(discord: 0) {
  >     profile {
  >       status {
  >         gear {
  >           weapon {
  >             name
  >           }
  >         }
  >       }
  >     }
  >       errors {
  >         msg
  >       }
  >     }
  >   }
  > ```

  If there are no errors, you should see that the weapon name stored for this profile is `Nautilus 47`.

  You have sucessfully ran your first query!

### 5. To explore other parts of the profile, see the [proflies](profiles) page.