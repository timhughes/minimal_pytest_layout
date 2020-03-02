# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

from .context.mything.helpers import increment


def test_answer():
    assert increment(3) == 4
