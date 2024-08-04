from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich_menu import Menu
from tomlkit import dumps
import os
import re
import rich
import shutil
import typer

app = typer.Typer()
console = Console()

HOME = Path(os.path.expanduser("~")) 
CONFIG_DIR = f"{HOME}/.git-profile"
config_dir = Path(CONFIG_DIR)

@app.command()
def create(
    profile_name: str = typer.Option("default", help="The name of the git profile. For e.g., work. The default name for the profile will be `default`. If a profile name is not provided, the existing default profile will be replaced."), 
    username: str = typer.Option("default-user", help="The username to be used in this git profile. Default value will be `default-user`"),
    email: str = typer.Option(help="The email address to be used in the git profile. This field is required."), 
    signingkey: str = typer.Option("", help="The signing key to be used in this git profile. Must be a string. If you're using SSH key, copy the contents of the public key here.")
):
    if not config_dir.exists():
        config_dir.mkdir(parents=True)
    config = {
        "user": {
            "name": username,
            "email": email,
            "signingkey": signingkey
        }
    }
    with rich.progress.open(config_dir / f"{profile_name}.git-profile", "w") as f:
        f.write(dumps(config))


@app.command()
def use():
    if not config_dir.exists():
        console.error("No profiles found. Create one first")
        exit(1)
    _, _, files = next(os.walk(CONFIG_DIR))
    files = [re.sub(r"\.git-profile$", "", file) for file in files]
    menu = Menu(
        *files
    )
    profile = menu.ask()
    console.print(Markdown("Backing up current `.gitconfig` file to `.gitconfig.bak`"))
    shutil.copyfile(HOME / ".gitconfig", HOME / ".gitconfig.bak")
    console.print(Markdown("Copying the new `.git-profile` configuration to `~/.gitconfig`"))
    shutil.copyfile(config_dir / f"{profile}.git-profile", HOME / ".gitconfig")


@app.command()
def restore():
    console.print(Markdown("Restoring the old `.gitconfig` configuration"))
    shutil.copyfile(HOME / ".gitconfig.bak", HOME / ".gitconfig")



if __name__ == "__main__":
    app()