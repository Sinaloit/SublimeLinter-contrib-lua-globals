#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Patrick Kish
# Copyright (c) 2014 Patrick Kish
#
# License: MIT
#
"""This module exports the LuaGlobals plugin class."""

from os.path import dirname, realpath
LUA_PLUGIN = dirname(realpath(__file__))

from SublimeLinter.lint import Linter, util


class LuaGlobals(Linter):

    """Provides an interface to lua-globals."""

    syntax = 'lua'
    cmd = 'lua "' + LUA_PLUGIN + '/findglobals.lua" "@"'
    regex = (
        r'\s*\[(?P<line>\d+)\]\s+'
        r'((?P<warning>G:)|(?P<error>S:))'
        r'(?P<message>.+?(?::\s(?P<near>.*)|$))'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = "lua"
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
