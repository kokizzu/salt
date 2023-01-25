"""
These commands are used to generate Salt's manpages.
"""
# pylint: disable=resource-leakage,broad-except
from __future__ import annotations

import datetime
import fnmatch
import logging
import os
import pathlib
import shutil
import subprocess
import sys
import textwrap

import yaml
from ptscripts import Context, command_group

log = logging.getLogger(__name__)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

# Define the command group
doc = command_group(name="docs", help="Manpages tools", description=__doc__)

@doc.command(
    name="man",
)
def man(ctx: Context):
    #XXX tools update
    #ctx.run("make", "clean", cwd="doc/", check=True)
    #ctx.run("make", "man", "SHPINXOPTS=-W", cwd="doc/", check=True)
    os.chdir("doc/")
    ctx.run("make", "clean", check=True)
    ctx.run("make", "man", "SHPINXOPTS=-W", check=True)
    for root, dirs, files in os.walk("doc/_build/man"):
        for file in files:
            shutil.copy(os.path.join(root, file), os.path.join("doc/man", file))


@doc.command(
    name="html",
)
def html(ctx: Context):
    ctx.run("make", "clean", cwd="doc/", check=True)
    ctx.run("make", "html", "SHPINXOPTS=-W", cwd="doc/", check=True)


@doc.command(
    name="epub",
)
def epub(ctx: Context):
    ctx.run("make", "clean", cwd="doc/", check=True)
    ctx.run("make", "epub", "SHPINXOPTS=-W", cwd="doc/", check=True)


@doc.command(
    name="pdf",
)
def html(ctx: Context):
    if not shutil.which("inkscape"):
        ctx.warn("No inkscape binary found")
        ctx.exit(1)
    ctx.run("make", "clean", cwd="doc/", check=True)
    ctx.run("make", "pdf", "SHPINXOPTS=-W", cwd="doc/", check=True)