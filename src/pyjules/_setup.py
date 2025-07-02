from os import PathLike
import subprocess

def setup(image_file: str | PathLike, name: str = "JULES") -> None:
    """
    Perform a one-time setup for running dockerised JULES.

    This function goes through the following steps:

    1. `udocker install` to set up udocker.
    2. `udocker load` to load an image from `image_file`.
    3. `udocker verify` to check the loaded image isn't corrupted.

    Args:
      image_file: A `.tar` containing the image, created using `docker save`.
      name: A name for the image.
    """
    # NOTE: could use udocker python API directly
    # TODO: handle stdout/stderr

    subprocess.run(
        ["udocker", "-D", "install"],
    )

    subprocess.run(
        ["udocker", "--allow-root", "load", "-i", image_file, name],
    )

    subprocess.run(
        ["udocker", "verify", name],
    )


