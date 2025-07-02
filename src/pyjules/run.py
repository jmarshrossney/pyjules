from os import PathLike
import pathlib
import subprocess

class InvalidPath(Exception):
    pass

class InvalidName(Exception):
    pass

def run(run_dir: str | PathLike, namelists_dir: str | PathLike | None = None, container_name: str = "JULES") -> None:
    """
    Run a containerised version of JULES.

    Must run `pyjules.setup` first.

    Args:
      run_dir: Path to the directory in which the jules executable will be run.
      namelists_dir: Path to the directory containing the namelists.
      container_name: The name of the container to be run.
    """
    # Check valid name (possibly overkill)
    try: 
        subprocess.run(
            ["udocker", "inspect", container_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise InvalidName(exc.stderr) from exc

    cwd = pathlib.Path.cwd()
    run_dir = Path(run_dir).resolve()
    namelists_dir = run_dir if namelists_dir is None else Path(namelists_dir).resolve()

    # We will mount the cwd when running the container. Hence, run_dir and
    # namelists_dir must be subdirectories of cwd!
    if not (run_dir.is_relative_to(cwd) and namelists_dir.is_relative_to(cwd)):
        msg = f"Both `run_dir` and `namelists_dir` must be subdirectories of the current working directory, {cwd}!"
        raise InvalidPath(msg)
    
    run_dir = run_dir.relative_to(cwd)
    namelists_dir = namelists_dir.relative_to(cwd)

    # This is where the cwd will end up in the container filesystem
    mount_point = pathlib.Path("/run")

    subprocess.run(
        [
            "udocker",
            "run",
            "-v",
            f"{cwd}:{mount_point}",
            container_name,
            "-d",
            mount_point / working_dir,
            mount_point / namelists_dir
        ],
    )
