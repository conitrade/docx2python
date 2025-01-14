#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""Test symbol extraction.

:author: Shay Hill
:created: 11/2/2021

Symbols are captured in the docx content files as ``<sym>`` elements.

```
    <w:document>
        <w:body>
            <w:p>
                <w:r>
                    <w:sym w:font="Symbol" w:char="F0F0"/>
                </w:r>
            </w:p>
        </w:body>
    </w:document>
```
"""


from .conftest import RESOURCES
from docx2python.main import docx2python


def test_symbols() -> None:
    """Export symbols as span elements."""
    pars = docx2python(RESOURCES / "symbols.docx")
    assert pars.text == (
        "<span style=font-family:Webdings>&#x0068;</span>"
        "≠"
        "<span style=font-family:Symbol>&#x00F0;</span>"
        "∞×÷≥≤±™®©¥£€µαβπΩ∑"
        "<span style=font-family:Webdings>&#x004A;</span>"
        "<span style=font-family:Webdings>&#x004B;</span>"
        "<span style=font-family:Webdings>&#x0084;</span>"
        "<span style=font-family:Webdings>&#x00E6;</span>"
        "<span style=font-family:Webdings>&#x00DD;</span>"
    )


def test_symbols_with_html_true() -> None:
    """Export symbols as span elements."""
    pars = docx2python(RESOURCES / "symbols.docx", html=True)
    assert pars.text == (
        "<span style=font-family:Webdings>&#x0068;</span>"
        "≠"
        "<span style=font-family:Symbol>&#x00F0;</span>"
        "∞×÷≥≤±™®©¥£€µαβπΩ∑"
        "<span style=font-family:Webdings>&#x004A;</span>"
        "<span style=font-family:Webdings>&#x004B;</span>"
        "<span style=font-family:Webdings>&#x0084;</span>"
        "<span style=font-family:Webdings>&#x00E6;</span>"
        "<span style=font-family:Webdings>&#x00DD;</span>"
    )
