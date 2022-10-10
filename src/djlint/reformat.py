"""Djlint reformat html files.

Much code is borrowed from https://github.com/rareyman/HTMLBeautify, many thanks!
"""

import difflib
from pathlib import Path

from .formatter.compress import compress_html
from .formatter.condense import condense_html
from .formatter.css import format_css
from .formatter.expand import expand_html
from .formatter.indent import indent_html
from .formatter.js import format_js
from .settings import Config
import logging


def reformat_file(config: Config, this_file: Path) -> dict:
    """Reformat html file."""
    logging.basicConfig(level="DEBUG", filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    rawcode = this_file.read_text(encoding="utf8")

    compressed = compress_html(rawcode, config)
    logging.debug(f"\nCOMPRESSED\n{compressed}")

    expanded = expand_html(compressed, config)
    logging.debug(f"\nEXPANDED\n{expanded}")

    condensed = condense_html(expanded, config)
    logging.debug(f"\nCONDENSED\n{condensed}")

    beautified_code = indent_html(condensed, config)
    logging.debug(f"\nBEAUTIFIED\n{beautified_code}")

    if config.format_css:
        beautified_code = format_css(beautified_code, config)

    if config.format_js:
        beautified_code = format_js(beautified_code, config)

    if config.check is not True:
        # update the file
        this_file.write_text(beautified_code, encoding="utf8")

    out = {
        str(this_file): list(
            difflib.unified_diff(rawcode.splitlines(), beautified_code.splitlines())
        )
    }
    return out
