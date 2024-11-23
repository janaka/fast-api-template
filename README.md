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