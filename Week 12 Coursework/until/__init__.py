"""
Top-level package interface for until.

This package exposes the main grid classes defined in grids.py so that they
can be imported directly from until.

Exports
-------
Grid
    Base occupancy grid class.
UniformGrid
    Grid with exactly two occupancies in every row and column.
NTiL
    Grid satisfying the no-three-in-line condition.
UNTiL
    Grid satisfying both the uniformity and no-three-in-line conditions.
"""

from .grids import Grid, UniformGrid, NTiL, UNTiL, til

__all__ = ["Grid", "UniformGrid", "NTiL", "UNTiL"]