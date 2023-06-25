"""
Pyrography - A wonderful Pyrogram fork inspired by Pyromod & AmanoTeam/Pyrogram.
Copyright (C) 2023-present Lelzin λ <https://github.com/d3cryptofc>

Forked from Pyrogram <https://github.com/pyrogram/pyrogram>,
originally copyright (C) 2017-present Dan <https://github.com/delivrance>

This file is part of Pyrography.

Pyrography is is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

Pyrography is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
for more details.

You should have received a copy of the GNU Lesser General Public License along
with Pyrography. If not, see <http://www.gnu.org/licenses/>.
"""

from io import BytesIO
from typing import Any

from .primitives.int import Int, Long
from .tl_object import TLObject


class FutureSalt(TLObject):
    ID = 0x0949D9DC

    __slots__ = ["valid_since", "valid_until", "salt"]

    QUALNAME = "FutureSalt"

    def __init__(self, valid_since: int, valid_until: int, salt: int):
        self.valid_since = valid_since
        self.valid_until = valid_until
        self.salt = salt

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "FutureSalt":
        valid_since = Int.read(data)
        valid_until = Int.read(data)
        salt = Long.read(data)

        return FutureSalt(valid_since, valid_until, salt)

    def write(self, *args: Any) -> bytes:
        b = BytesIO()

        b.write(Int(self.valid_since))
        b.write(Int(self.valid_until))
        b.write(Long(self.salt))

        return b.getvalue()
