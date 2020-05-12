# :shell: `nautilus-chambers`
> A service/API for storing and synchronizing Splatoon 2 user profiles across multiple discord bots.

![License][license-shield]
![Stars][stars-shield]
# <!-- ![Banner](https://github.com/LeptoFlare/PROJECTNAME/banner.png) -->

Nautilus is a Public API/database holds Splatoon 2 profile data on users. Powered by Python, GraphQL, MongoDB, Flask, Ariadne, and Pydantic. Use this API with your discord bot to:
- Store user data without the need of your own database.
- Synchronize user data from anywhere, no matter the bot.

## Usage <!-- Using the project directly -->
_Documentation can me found [here](https://github.lepto.tech/nautilus-chambers/docs)._
  
```python
import requests

# POST request to get data from api endpoint
# Changes frequently at this current stage in development.
# That's why there isn't actual code here for now.
```

## Contributing <!-- Using the source code -->
1. Fork the repository and clone it.
2. Make a new branch to submit your pull request from.

### Running locally
1. Create a `config.yml` in the repository root:
   ```yml
   debug: true
   ```
2. Run `docker-compose up --build` in the repository root.

---

Contact me · [**@LeptoFlare**](https://github.com/LeptoFlare) · [lepto.tech](https://lepto.tech/)

As always, distributed under the MIT license. See `LICENSE` for more information.

_[https://github.com/LeptoFlare/nautilus-chambers](https://github.com/LeptoFlare/nautilus-chambers)_

<!-- markdown links & imgs -->
[stars-shield]: https://img.shields.io/github/stars/LeptoFlare/nautilus-chambers.svg?style=social
[license-shield]: https://img.shields.io/github/license/LeptoFlare/nautilus-chambers.svg?style=flat
