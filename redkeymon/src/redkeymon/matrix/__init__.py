"""
matrix subpackage

Exposes elementary row-operation utilities (rowswap, rowscale,
rowreplacement) and the rref() routine built on top of them.
"""

from .elementary import rowswap, rowscale, rowreplacement, rref

__all__ = ["rowswap", "rowscale", "rowreplacement", "rref"]
