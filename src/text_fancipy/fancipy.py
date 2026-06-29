#!/usr/bin/env python3
# this_file: src/text_fancipy/fancipy.py
"""Core conversion logic for text_fancipy.

Unicode Mathematical Alphanumeric Symbols (U+1D400–U+1D7FF) form contiguous
runs of styled A-Za-z glyphs.  Each style simply shifts the ASCII code-point
of every letter by a fixed offset, making forward and reverse tables trivial to
build arithmetically.  Accented Latin characters are handled via NFD
decomposition: the base letter is shifted by the table; combining marks (which
are not in A-Za-z) pass through unchanged; NFC recomposition rebuilds the
accented glyph afterward.
"""

import logging

try:
    import unicodedata2 as unicodedata  # faster drop-in replacement
except ImportError:
    import unicodedata  # stdlib fallback


__author__ = "Adam Twardoch"
__copyright__ = "(c) 2023 Adam Twardoch"
__license__ = "Apache-2.0"

_logger = logging.getLogger(__name__)

# Type alias: (forward_table, reverse_table, fancy_display_name)
_TableEntry = tuple[dict[int, int], dict[int, int], str]


def create_tables() -> dict[str, _TableEntry]:
    """Build forward and reverse translation tables for every supported style.

    Each style is defined by the Unicode code-point of its styled 'A' (upper)
    and 'a' (lower).  All other letters are computed by simple arithmetic
    relative to those anchors, which mirrors the contiguous layout of the
    Unicode Mathematical Alphanumeric Symbols block (U+1D400–U+1D7FF) and
    the Enclosed Alphanumerics block (U+2460–U+24FF, U+1F110–U+1F12F) for
    circled and parenthesised variants.

    Only styles that provide full A-Za-z coverage in Unicode 15.0 are included.

    Returns:
        A dict mapping style code → (forward_table, reverse_table, fancy_name).
    """
    # Each entry: (first_uppercase_char, first_lowercase_char, fancy_display_name)
    styles: dict[str, tuple[str, str, str]] = {
        "dflt": ("A", "a", "Default"),
        # Unicode Mathematical Alphanumeric Symbols block (U+1D400–U+1D7FF)
        "mono": ("𝙰", "𝚊", "𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎"),
        "bold": ("𝐀", "𝐚", "𝐒𝐞𝐫𝐢𝐟 𝐁𝐨𝐥𝐝"),
        "bdit": ("𝑨", "𝒂", "𝑺𝒆𝒓𝒊𝒇 𝑩𝒐𝒍𝒅 𝑰𝒕𝒂𝒍𝒊𝒄"),
        "sans": ("𝖠", "𝖺", "𝖲𝖺𝗇𝗌"),
        "snbd": ("𝗔", "𝗮", "𝗦𝗮𝗻𝘀 𝗕𝗼𝗹𝗱"),
        "snit": ("𝘈", "𝘢", "𝘚𝘢𝘯𝘴 𝘐𝘵𝘢𝘭𝘪𝘤"),
        "snbi": ("𝘼", "𝙖", "𝙎𝙖𝙣𝙨 𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘"),
        "scrb": ("𝓐", "𝓪", "𝓢𝓬𝓻𝓲𝓹𝓽 𝓑𝓸𝓵𝓭"),
        "frak": ("𝕬", "𝖆", "𝕱𝖗𝖆𝖐𝖙𝖚𝖗 𝕭𝖔𝖑𝖉"),
        # Enclosed Alphanumerics / Enclosed Alphanumeric Supplement
        "parn": ("🄐", "⒜", "🄟⒜⒭⒠⒩⒮"),  # parenthesised
        "circ": ("Ⓐ", "ⓐ", "Ⓒⓘⓡⓒⓛⓔⓓ"),  # circled
        # Fullwidth Latin (U+FF21–U+FF3A, U+FF41–U+FF5A)
        "wide": ("Ａ", "ａ", "Ｗｉｄｅ"),
    }

    tables: dict[str, _TableEntry] = {}
    for s, (uc, lc, fancy_name) in styles.items():
        # Build forward mapping: ASCII ordinal → styled ordinal
        uc_offset = ord(uc) - ord("A")
        lc_offset = ord(lc) - ord("a")
        forward: dict[int, int] = {}
        for i in range(ord("A"), ord("Z") + 1):
            forward[i] = i + uc_offset
        for i in range(ord("a"), ord("z") + 1):
            forward[i] = i + lc_offset

        # Reverse mapping: styled ordinal → ASCII ordinal
        reverse: dict[int, int] = {v: k for k, v in forward.items()}

        tables[s] = (
            str.maketrans(forward),
            str.maketrans(reverse),
            fancy_name,
        )

    return tables


_precomputed_tables: dict[str, _TableEntry] = create_tables()


def get_table(style: str, reverse: bool) -> dict[int, int]:
    """Return the translation table for *style* in the requested direction.

    Args:
        style: Style code, e.g. ``"bold"``, ``"mono"``.  Falls back to the
            identity table (``"dflt"``) when the code is unknown.
        reverse: ``False`` for forward (plain → fancy), ``True`` for reverse
            (fancy → plain).

    Returns:
        A :func:`str.maketrans`-style mapping dict suitable for
        :meth:`str.translate`.
    """
    entry = _precomputed_tables.get(style) or _precomputed_tables["dflt"]
    # Index 0 = forward, 1 = reverse
    return entry[int(reverse)]  # type: ignore[return-value]


def fancipy(text: str, style: str) -> str:
    """Convert plain ASCII letters in *text* to the requested Unicode style.

    Non-letter characters (digits, punctuation, spaces) are passed through
    unchanged.  Accented Latin characters survive the round-trip: NFD
    decomposition separates the base letter from its combining marks; only the
    base letter is shifted by the style table; NFC recomposition reconstructs
    the accented glyph.

    Args:
        text: Input text.  May contain any Unicode characters.
        style: Target style code.  One of the keys in
            :data:`_precomputed_tables` (e.g. ``"bold"``, ``"scrb"``).

    Returns:
        Text with A-Za-z replaced by their styled equivalents.
    """
    decomposed: str = unicodedata.normalize("NFD", text)
    converted: str = decomposed.translate(get_table(style, False))
    return str(unicodedata.normalize("NFC", converted))


def unfancipy(text: str, style: str) -> str:
    """Reverse a specific style, converting fancy letters back to plain ASCII.

    Args:
        text: Fancy-styled text.
        style: The style to undo.  Must match the style used during
            :func:`fancipy`.

    Returns:
        Text with styled characters replaced by their ASCII equivalents.
    """
    decomposed: str = unicodedata.normalize("NFD", text)
    converted: str = decomposed.translate(get_table(style, True))
    return str(unicodedata.normalize("NFC", converted))


def unfancipy_all(text: str) -> str:
    """Strip every known style, converting all fancy letters back to plain ASCII.

    Applies :func:`unfancipy` for every registered style in sequence.  Safe to
    call on text that mixes multiple styles or contains no styled characters at
    all.

    Args:
        text: Text potentially containing any mix of styled Unicode letters.

    Returns:
        Plain ASCII text with all known styles removed.
    """
    for style in _precomputed_tables:
        text = unfancipy(text, style)
    return text
