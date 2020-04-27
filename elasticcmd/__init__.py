"""Top-level package for elasticcmd."""

__author__ = """Yuriy Halytskyy"""
__email__ = 'yuriy.halytskyy@gmail.com'
__version__ = '0.1.0'

import readline
from enum import Enum
from traitlets import UseEnum, Unicode, HasTraits, observe

class Mode(Enum):
    GLOBAL = 1
    QUERY = 2

class CommandParser:

    def __init__(self,cmd):
        self.cmd = cmd

    def exec(self, input: str):

        tokens = input.split()
        if (tokens[0] == "set"):
            setattr(self.cmd, tokens[1],tokens[2])
            return

        raise ParseError(f"'{input}' not understood")

class ElasticCmd(HasTraits):

    mode = UseEnum(Mode, default_value=Mode.GLOBAL)

    index = Unicode("").tag(config=True)


    @observe('mode')
    def _mode_changed(self, change):
        if (self.index == "" and change['new'] == Mode.QUERY):
            raise CmdWarning("enter query mode without an index set")

    pass


class CmdWarning(Exception):
    """
    This exception is thrown when an operation on ElasticCmd will put it in the
    state that might cause issues for the user.

    For example, an attempt to set ElasticCmd to query mode without an index set
    will raise CmdWarning. The operation will still be completed.
    """

class ParseError(Exception):
    """
    This exception is thrown when command parser cannot make sense of the input
    """



if __name__ == "__main__":
    while True:
        i = input("[cmd] ")
