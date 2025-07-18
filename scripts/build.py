#!/usr/bin/env python3
"""Build script for text_fancipy package."""

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

def build_package():
    """Build Python package."""
    print("Building Python package...")
    return run_command([sys.executable, "-m", "build"])

def main():
    parser = argparse.ArgumentParser(description="Build text_fancipy package")
    parser.add_argument("--python", action="store_true", help="Build Python package")
    parser.add_argument("--all", action="store_true", help="Build everything")
    
    args = parser.parse_args()
    
    if args.python or args.all:
        if not build_package():
            sys.exit(1)
    
    print("Build completed successfully!")

if __name__ == "__main__":
    main()