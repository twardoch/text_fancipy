#!/usr/bin/env python3
"""Comprehensive test suite for text_fancipy."""

import os
import sys
import pytest

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from text_fancipy.fancipy import fancipy, unfancipy_all, _precomputed_tables

def test_all_styles_available():
    """Test that all expected styles are available."""
    expected_styles = {
        'dflt', 'mono', 'bold', 'bdit', 'sans', 'snbd', 
        'snit', 'snbi', 'scrb', 'frak', 'parn', 'circ', 'wide'
    }
    assert set(_precomputed_tables.keys()) == expected_styles

def test_style_conversions():
    """Test style conversions."""
    test_text = "Hello World"
    
    for style in _precomputed_tables.keys():
        if style == 'dflt':
            assert fancipy(test_text, style) == test_text
        else:
            result = fancipy(test_text, style)
            assert result != test_text
            assert len(result) == len(test_text)

def test_round_trip():
    """Test round trip conversions."""
    test_text = "Hello World"
    
    for style in _precomputed_tables.keys():
        if style == 'dflt':
            continue
        
        fancy = fancipy(test_text, style)
        restored = unfancipy_all(fancy)
        
        # Basic letters should be preserved
        assert 'Hello World' in restored or 'Hello' in restored

def test_edge_cases():
    """Test edge cases."""
    # Empty string
    assert fancipy("", "bold") == ""
    
    # Numbers and symbols
    test_text = "123!@#"
    assert fancipy(test_text, "bold") == test_text

if __name__ == '__main__':
    pytest.main([__file__, '-v'])