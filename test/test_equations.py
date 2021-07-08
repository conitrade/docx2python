#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""Pull some information from equations

:author: Shay Hill
:created: 7/7/2021

User sreeroopnaidu requested equation export. Equations are made up internally of
<w:m> elements. Previous versions of Docx2Python ignored these elements. These are now recognized.

Equations in Word's Professional format will return garbage.
Equations in Word's Inline format will return a nice string.
"""

from pathlib import Path

from docx2python import docx2python

TEST_DOCX = Path(__file__, "../resources/equations.docx")


class TestEquations:
    def test_professional_format(self):
        """
        Start a new paragraph when a <w:br/> element is found.
        """
        body = docx2python(TEST_DOCX, html=True).body
        assert body == [
            [[["Professional Format", "01x", "Linear Format", "\\int_{0}^{1}x"]]]
        ]