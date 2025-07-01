import pathlib
import subprocess

def run(working_dir: str, config_dir: str | None = None, container_name: str = "jules") -> None:
    """
    Run Jules.
    """

    cwd = pathlib.Path.cwd()
    working_dir = working_dir.relative_to(cwd)
    config_dir = config_dir.relative_to(cwd)

    subprocess.run(
        ["udocker", "run", "-v", f"{cwd}:/run", container_name, "-d", working_dir, config_dir],
    )
