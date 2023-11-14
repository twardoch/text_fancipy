#!/usr/bin/env python3

import fire
import sys
from pathlib import Path
from .fancipy import fancipy, unfancipy_all, _precomputed_tables


def convert(text=None, file=None, style="dflt", reverse=False, outfile=None):
    if file:
        with open(file, "r", encoding="utf-8") as f:
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
    """Converts plain English letters (A-Za-z) in -t TEXT or -f -FILE to Unicode counterparts in a specified fancy style, or converts all fancy-styled text back to plain text, and writes to -o FILE or prints."""

    def __init__(self):
        for style in _precomputed_tables.keys():
            setattr(self, style, self._create_style_method(style))

    def _create_style_method(self, style):
        def style_method(text=None, file=None, outfile=None):
            return convert(text, file, style, False, outfile)

        style_method.__doc__ = f"Convert to {_precomputed_tables[style][2]} style"
        return style_method

    def undo(self, text=None, file=None, outfile=None):
        """
        Convert fancy-styled text back to plain text
        """
        return convert(text, file, "dflt", True, outfile)

    def show(self):
        """
        Show available styles in a Markdown table format with appropriate padding.
        """
        # Find the length of the longest fancified style name
        longest_name_length = max(len(fancy_name) for _, _, fancy_name in _precomputed_tables.values())

        # Create the table headers with appropriate padding
        print("| style  | name" + " " * (longest_name_length - 4) + " |")
        print("|--------|" + "-" * (longest_name_length + 2) + "|")

        # Print each row with padding adjusted to the longest name
        for style, (_, _, fancy_name) in sorted(_precomputed_tables.items()):
            padding = " " * (longest_name_length - len(fancy_name))
            print(f"| `{style}` | {fancy_name}{padding} |")

def cli():
    fancipy_cli = FanciPyCLI()
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(fancipy_cli)


if __name__ == "__main__":
    cli()
