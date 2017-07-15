#!/bin/env python
# -*- coding: utf-8 -*-
#
import fontforge

from pprint import pprint

# srcf = fontforge.open("ipaexg.ttf")
srcf = fontforge.open("IPAexGothic.sfd")
dstf = srcf

srcglyphs = srcf.glyphs()
for item in srcglyphs:
    prop = item.getPosSub("'trad' Traditional Forms lookup 19 subtable")

    # skip < U+2E80 ; not kanji area
    enc = item.encoding
    if enc < 0x2E80:
        continue

    if len(prop) != 0:
        curfname = item.glyphname
        subfname = prop[0][2]
        srcf.selection.select(subfname)
        srcf.copy()
        dstf.selection.select(curfname)
        dstf.paste()

dstf.save("mod.sfd")

