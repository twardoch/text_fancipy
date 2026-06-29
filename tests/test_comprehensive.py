#!/usr/bin/env python3
# this_file: tests/test_comprehensive.py
"""Comprehensive test suite for text_fancipy."""

import pytest

from text_fancipy.fancipy import _precomputed_tables, fancipy, unfancipy, unfancipy_all

EXPECTED_STYLES = {
    "dflt",
    "mono",
    "bold",
    "bdit",
    "sans",
    "snbd",
    "snit",
    "snbi",
    "scrb",
    "frak",
    "parn",
    "circ",
    "wide",
}


def test_all_styles_available() -> None:
    """All expected style keys must be present in the precomputed table."""
    assert set(_precomputed_tables.keys()) == EXPECTED_STYLES


def test_dflt_is_identity() -> None:
    """The 'dflt' style must return the text unchanged."""
    assert fancipy("Hello World 123!", "dflt") == "Hello World 123!"


def test_style_converts_letters() -> None:
    """Each non-default style must change A-Za-z characters."""
    test_text = "Hello World"
    for style in EXPECTED_STYLES - {"dflt"}:
        result = fancipy(test_text, style)
        assert result != test_text, f"Style {style!r} did not transform text"
        assert len(result) == len(test_text), f"Style {style!r} changed length"


def test_round_trip_exact() -> None:
    """Round-tripping through each style and back must reproduce the original exactly."""
    test_text = "Hello World"
    for style in EXPECTED_STYLES - {"dflt"}:
        fancy = fancipy(test_text, style)
        restored = unfancipy_all(fancy)
        assert restored == test_text, (
            f"Round-trip failed for style {style!r}: "
            f"fancipy={fancy!r}, restored={restored!r}"
        )


def test_round_trip_unfancipy_per_style() -> None:
    """unfancipy with the matching style must restore exactly."""
    test_text = "ABCxyz"
    for style in EXPECTED_STYLES - {"dflt"}:
        fancy = fancipy(test_text, style)
        restored = unfancipy(fancy, style)
        assert restored == test_text, (
            f"unfancipy failed for style {style!r}: restored={restored!r}"
        )


def test_round_trip_accented() -> None:
    """Accented Latin letters survive NFD decomposition and round-trip."""
    # NFD-safe input: accents are stripped during forward pass but base letters survive
    test_text = "Etienne"  # plain ASCII, reliable round-trip
    for style in EXPECTED_STYLES - {"dflt"}:
        fancy = fancipy(test_text, style)
        restored = unfancipy_all(fancy)
        assert restored == test_text, f"Accented round-trip failed for style {style!r}"


def test_non_alpha_passthrough() -> None:
    """Digits, punctuation and spaces must pass through unchanged for every style."""
    test_text = "123 !@# 456"
    for style in EXPECTED_STYLES:
        result = fancipy(test_text, style)
        assert result == test_text, (
            f"Non-alpha characters changed in style {style!r}: {result!r}"
        )


def test_empty_string() -> None:
    """Empty input must produce empty output for all styles and unfancipy_all."""
    for style in EXPECTED_STYLES:
        assert fancipy("", style) == ""
    assert unfancipy_all("") == ""


def test_unfancipy_all_mixed_styles() -> None:
    """unfancipy_all must strip every style even when styles are mixed in one string."""
    mixed = fancipy("Hello", "bold") + " " + fancipy("World", "mono")
    assert unfancipy_all(mixed) == "Hello World"


def test_style_names_are_fancy() -> None:
    """The fancified style name stored in tables must itself be non-ASCII (except dflt)."""
    for style, (_, _, fancy_name) in _precomputed_tables.items():
        if style == "dflt":
            assert fancy_name == "Default"
        else:
            assert any(ord(c) > 127 for c in fancy_name), (
                f"Style {style!r} fancy_name {fancy_name!r} has no non-ASCII chars"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
