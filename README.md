![git](https://github.com/user-attachments/assets/dbff33a0-d63b-4b86-ac64-7c1c210a1515)

# Git Profile Switcher

Used to switch between different `git` profiles or configurations easily.

## Usage

### List all the commands available

```text
$ poetry run python3 main.py --help
  create              This is used to create a new profile. Initially it will create a directory ~/.git-profile where all the profiles will be stored. 
  use                 This is used to switch to a different profile. This creates a backup of the current ~/.gitconfig file to ~/.gitconfig.bak
  restore             This is used to restore the previous ~/.gitconfig which is currently at ~/.gitconfig.bak
```

### Commands

#### `create`

```text
$ poetry run python3 main.py create --help
  --profile-name      The name of the git profile. For e.g., work. The default name for the profile will be `default`. If a profile name is not provided, the
                      existing default profile  will be replaced.
  --username          The username to be used in this git profile. Default value will be `default-user`
  --email             The email address to be used in the git profile. This field is required. [default: None] [required]
  --signingkey        The signing key to be used in this git profile. Must be a string. If you're using SSH key, copy the contents of the public key here.
  --help              Show this message and exit.
```

`create` has $5$ options.

- `--profile-name`: This is the profile name to be used for the git profile. For e.g., if you want to create a new profile for `work`, just give the value as `work`.
- `--username`: Your full name to be used during commits.
- `--email`: E-Mail to be used for commits.

#### `use`

```sh
$ poetry run python3 main.py use
```

`use` has no options. It will give a terminal menu via which you shall select a git profile to use. The old `~/.gitconfig` will be backed up to `~/.gitconfig.bak` before changing the profile.

#### `restore`

```sh
$ poetry run python3 main.py restore
```

`restore` command just restores old git configuration i.e. restores `~/.gitconfig.bak` to `~/.gitconfig`
