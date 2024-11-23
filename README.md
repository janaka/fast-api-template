# FastAPI Template Application

Either, Use the Github create from template feature. 

Or

- Clone this repo
- Delete .git folder `rm -rf .git/`
- Rename the repo folder `mv fast-api-template <your new application name>`
- Change name, author, repo etc in the project.toml file.
- (Optional) if you need a mono repo because of other components like a shared module, cli, web app etc. create a folder in the root and move `src`, `.gitignore`, and `project.toml` to that folder.
- `git init` etc. to create a new repo.


## Contributing

### Requirements

- poetry `pip install poetry`

### Run locally

- `poetry install`
- `poe start-dev`

### Expose local instnace externally

`npx localtunnel --subdomain vlm-janaka --port 8000 --print-requests true`

## Licensing

This template repository is provided without any specific licensing restrictions on the application code you create from it. You are encouraged to choose any license that fits your project's needs.

### Common License Options

- **MIT License**: A permissive license that allows for reuse with minimal restrictions.
- **Apache License 2.0**: Similar to MIT but includes provisions for patents.
- **GNU General Public License (GPL)**: Requires derivative works to also be open-sourced under the same license.
- **BSD License**: Permissive like MIT, but with additional clauses regarding attribution.

For more information on choosing a license, visit [ChooseALicense.com](https://choosealicense.com).