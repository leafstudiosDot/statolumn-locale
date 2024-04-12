# Statolumn Language Translation Contribution
Contribute your fluent language to translate Statolumn.

## How to contribute
### Language Translation
If you want to contribute to the language translation, you can contribute by following these steps:
1. Fork this repository
2. `python3 genlocale.py <lang>` to generate a new language file based from the English `en.json`. Replace `<lang>` with your language code such as `'en'`, `'es'`, `'jp'`.
3. Translate the generated `<lang>.json` file, make sure you translate only the value.
4. Submit a pull request to this repository.

### Trusted Links
This can be a very serious issue when it comes to links that contains redirect, so we need to be careful about this and we have a policy for this.

If you want to add a trusted link, you can do it by following these steps:
1. Fork this repository
2. Add the link in the `"trusted"` array list in the `trusted_links.json` file.
3. Submit a pull request to this repository.

Thank you for your contribution, this makes non-English users have ease of access while using Statolumn!