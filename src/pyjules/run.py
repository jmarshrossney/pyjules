import pathlib
import subprocess

def run(working_dir: str, config_dir: str | None = None, container_name: str = "jules") -> None:
    """
    Run Jules.
    """

    cwd = pathlib.Path.cwd()
    working_dir = pathlib.Path(working_dir).resolve().relative_to(cwd)
    config_dir = pathlib.Path(config_dir).resolve().relative_to(cwd)

    subprocess.run(
        ["udocker", "run", "-v", f"{cwd}:/run", container_name, "-d", f"/run/{working_dir}" , f"/run/{config_dir}"],
    )
