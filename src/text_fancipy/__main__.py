#!/usr/bin/env python3
# this_file: src/text_fancipy/__main__.py
"""CLI entry-point for text_fancipy (via python-fire)."""

import sys
from typing import Callable, Optional

import fire  # type: ignore[import-untyped]

from .fancipy import _precomputed_tables, fancipy, unfancipy_all


def convert(
    text: Optional[str] = None,
    file: Optional[str] = None,
    style: str = "dflt",
    reverse: bool = False,
    outfile: Optional[str] = None,
) -> None:
    """Convert text and write result to stdout or a file."""
    if file:
        with open(file, encoding="utf-8") as f:
            text = f.read()

    if text is None:
        text = sys.stdin.read()

    result = unfancipy_all(text) if reverse else fancipy(text, style)

    if outfile:
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)


class FanciPyCLI:
    """Converts plain English letters (A-Za-z) in -t TEXT or -f FILE to Unicode counterparts in a specified fancy style, or converts all fancy-styled text back to plain text, and writes to -o FILE or prints."""

    def __init__(self) -> None:
        for style in _precomputed_tables:
            setattr(self, style, self._create_style_method(style))

    def _create_style_method(self, style: str) -> Callable[..., None]:
        def style_method(
            text: Optional[str] = None,
            file: Optional[str] = None,
            outfile: Optional[str] = None,
        ) -> None:
            return convert(text, file, style, False, outfile)

        style_method.__doc__ = f"Convert to {_precomputed_tables[style][2]} style"
        return style_method

    def undo(
        self,
        text: Optional[str] = None,
        file: Optional[str] = None,
        outfile: Optional[str] = None,
    ) -> None:
        """Convert fancy-styled text back to plain text."""
        return convert(text, file, "dflt", True, outfile)

    def show(self) -> None:
        """Show available styles in a Markdown table format with appropriate padding."""
        longest_name_length = max(
            len(fancy_name) for _, _, fancy_name in _precomputed_tables.values()
        )
        print("| style  | name" + " " * (longest_name_length - 4) + " | letters")
        print("|--------|" + "-" * (longest_name_length + 2) + "| ---------")
        for style, (_, _, fancy_name) in _precomputed_tables.items():
            padding = " " * (longest_name_length - len(fancy_name))
            style_letters = "".join(
                chr(u) for u in _precomputed_tables[style][False].values()
            )
            print(f"| `{style}` | {fancy_name}{padding} | {style_letters}")


def cli() -> None:
    """Entry-point registered in pyproject.toml [project.scripts]."""
    fancipy_cli = FanciPyCLI()
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(fancipy_cli)


if __name__ == "__main__":
    cli()
