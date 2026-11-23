"""Competition entrypoint: publish the drawn front page into the output directory.

The image is shipped beside this script as ``entry.png`` and copied byte for byte,
so a run needs no Pillow and no network. Standard library only.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
ENV_VARS = ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR")
GRADER_DIR = Path("/output")
LOCAL_DIR = "out"


def script_dir() -> Path:
    """Directory holding this script, and therefore ``entry.png``."""
    return Path(__file__).resolve().parent


def source_path() -> Path:
    """Path of the checked-in image."""
    return script_dir() / SOURCE_NAME


def out_override(argv: list[str]) -> str | None:
    """Return the directory given by ``--out DIR`` or ``--out=DIR``, else ``None``.

    Raises:
        SystemExit: when ``--out`` carries no directory, with status 2.
    """
    for index, item in enumerate(argv):
        value: str | None = None
        if item == "--out":
            value = argv[index + 1] if index + 1 < len(argv) else ""
        elif item.startswith("--out="):
            value = item[len("--out=") :]
        if value is not None:
            if not value.strip():
                print("error: --out needs a directory", file=sys.stderr)
                raise SystemExit(2)
            return value.strip()
    return None


def output_dir(override: str | None = None) -> Path:
    """Output directory: ``--out``, then the environment, ``/output``, then ``out/``."""
    if override:
        return Path(override)
    for name in ENV_VARS:
        value = os.environ.get(name, "").strip()
        if value:
            return Path(value)
    if GRADER_DIR.is_dir():
        return GRADER_DIR
    return script_dir() / LOCAL_DIR


def publish(destination: Path) -> int:
    """Copy ``entry.png`` into ``destination`` and report the result on stderr.

    Returns:
        Process exit code: 0 on success, 1 when the source image is missing.
    """
    source = source_path()
    if not source.is_file():
        print(f"error: {source} is missing, run python3 artwork.py first", file=sys.stderr)
        return 1
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / SOURCE_NAME
    shutil.copyfile(source, target)
    size = target.stat().st_size
    print(f"wrote {target} ({size} bytes)", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Resolve the output directory, copy the image and return the exit code."""
    arguments = sys.argv[1:] if argv is None else argv
    return publish(output_dir(out_override(arguments)))


if __name__ == "__main__":
    raise SystemExit(main())
