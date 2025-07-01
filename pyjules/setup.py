import subprocess

def setup(image_path: str, image_name: str = "jules") -> None:
    """
    One-time setup for running Jules.

    1. Run `udocker install`
    2. Load container from .tar file
    3. Verify loaded container
    """
    # NOTE: could use udocker python API directly
    # TODO: handle stdout/stderr

    subprocess.run(
        ["udocker", "install"],
    )

    subprocess.run(
        ["udocker", "--allow-root", "load", "-i", image_path, image_name],
    )

    subprocess.run(
        ["udocker", "verify", image_name],
    )


