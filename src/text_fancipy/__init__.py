# this_file: src/text_fancipy/__init__.py
"""text_fancipy — Unicode fancy-text converter.

Converts standard English letters (A-Za-z) to Unicode decorative styles
(bold, italic, monospace, script, fraktur, circled, etc.) and back.
"""

from importlib.metadata import PackageNotFoundError, version

from text_fancipy.fancipy import fancipy, unfancipy, unfancipy_all

try:
    __version__ = version("text_fancipy")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = ["fancipy", "unfancipy", "unfancipy_all", "__version__"]
