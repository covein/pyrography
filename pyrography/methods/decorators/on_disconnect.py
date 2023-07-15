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

from typing import Callable

import pyrography


class OnDisconnect:
    def on_disconnect(self=None) -> Callable:
        """Decorator for handling disconnections.

        This does the same thing as :meth:`~pyrography.Client.add_handler` using the
        :obj:`~pyrography.handlers.DisconnectHandler`.
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrography.Client):
                self.add_handler(pyrography.handlers.DisconnectHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((pyrography.handlers.DisconnectHandler(func), 0))

            return func

        return decorator