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

from typing import Optional

from pyrography.filters import Filter


class FilterRunningHandlers:
    async def filter_running_handlers(self, filters: Optional[Filter] = None):
        """
        Apply filters to current running handlers.

        Parameters:
            filters (``Filter``, *optional*):
                The filter to apply.
                Defaults to None.

        Raises:
            TypeError: Invalid filter type.

        Yields:
            ``pyrography.dispatcher.RunningHandler``:
            Contains attributes for handler and update.
        """
        # Creating alias to running_handlers.
        running_handlers = self.dispatcher.running_handlers

        # Validating input type for `filters` .
        if not isinstance(filters, Filter):
            raise TypeError(
                f'Parameter `filters` must be {Filter} type, not {type(filters)}'
            )

        # Iterating current running handlers.
        for running in running_handlers:
            # Yield update if no filter has been defined
            # or if the filter returns True.
            if filters is None or await filters(self, running.update):
                yield running.update