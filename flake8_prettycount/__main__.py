#!/usr/bin/env python3
#
#  __main__.py
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#

# stdlib
import sys

# 3rd party
import click
from consolekit import CONTEXT_SETTINGS

# this package
from flake8_prettycount.application import Application

__all__ = ["main"]


@click.command(context_settings={"ignore_unknown_options": True, "allow_extra_args": True, **CONTEXT_SETTINGS})
@click.pass_context
def main(ctx: click.Context):
	"""
	Wrapper around flake8 providing a formatted count at the end.

	All options and arguments are passed through to flake8.
	"""

	app = Application()
	app.run(ctx.args[:])
	app.exit()


if __name__ == "__main__":
	sys.exit(main(obj={}))
