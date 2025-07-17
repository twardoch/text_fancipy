#!/usr/bin/env python3
"""Test script for text_fancipy package."""

import os
import sys
import subprocess
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

def run_command(cmd):
    """Run a command and return success."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=PROJECT_ROOT)
    return result.returncode == 0

def run_tests():
    """Run tests."""
    print("Running tests...")
    return run_command([sys.executable, "-m", "pytest", "tests/", "-v"])

def main():
    parser = argparse.ArgumentParser(description="Test text_fancipy package")
    parser.add_argument("--unit", action="store_true", help="Run unit tests")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    
    args = parser.parse_args()
    
    if args.unit or args.all:
        if not run_tests():
            sys.exit(1)
    
    print("All tests passed!")

if __name__ == "__main__":
    main()