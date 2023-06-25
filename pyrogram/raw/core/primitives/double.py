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
from struct import unpack, pack
from typing import cast, Any

from ..tl_object import TLObject


class Double(bytes, TLObject):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> float:
        return cast(float, unpack("d", data.read(8))[0])

    def __new__(cls, value: float) -> bytes:  # type: ignore
        return pack("d", value)
