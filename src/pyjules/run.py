import pathlib
import subprocess

def run(working_dir: str, config_dir: str | None = None, container_name: str = "jules") -> None:
    """
    Run Jules.
    """

    cwd = pathlib.Path.cwd()
    working_dir = pathlib.Path(working_dir).relative_to(cwd)
    config_dir = pathlib.Path(config_dir).relative_to(cwd)
    print(working_dir)
    print(config_dir)

    subprocess.run(
        ["udocker", "run", "-v", f"{cwd}:/run", container_name, "-d", working_dir, config_dir],
    )
