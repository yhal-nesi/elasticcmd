#!/usr/bin/env python

"""Tests for `elasticcmd` package."""

import pytest


from elasticcmd import ElasticCmd, CommandParser, Mode, CmdWarning, ParseError

@pytest.fixture
def simple_cmd():
    return ElasticCmd()

def test_starts_in_general_mode(simple_cmd):
    # we always start in GLOBAL mode
    assert simple_cmd.mode == Mode.GLOBAL

def test_move_to_query_mode_without_index_set(simple_cmd):
    with pytest.raises(CmdWarning) as e:
        simple_cmd.mode = Mode.QUERY
    # the mode is still changed
    assert simple_cmd.mode == Mode.QUERY

def test_move_to_query_mode_with_index_set(simple_cmd):
    simple_cmd.index = "test_index"
    simple_cmd.mode = Mode.QUERY
    assert simple_cmd.mode == Mode.QUERY

@pytest.fixture
def simple_parser():
    ecmd = ElasticCmd()
    return CommandParser(ecmd)

def test_set_index(simple_parser):
    simple_parser.exec("set index test_index")
    ecmd = simple_parser.cmd
    assert ecmd.index == "test_index"

def test_invalid_command(simple_parser):
    with pytest.raises(ParseError) as e:
        simple_parser.exec("hello world")
