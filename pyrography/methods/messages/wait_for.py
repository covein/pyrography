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

import asyncio
import time
from pyrography.types import Update, Message
from pyrography.filters import Filter


class WaitFor:
    async def wait_for(self,
                       type: Update | None = Message,
                       filter: Filter | None = None,
                       timeout: int | None = 60):
        """
        Waits for a dispatcher update.

        Optional Args:
            type (Update):
                Type of update to receive, by default are text
                messages, if None any type will be received.

            filter (Filter | None):
                Specific filter for the update, by default
                there is no filter.

            timeout (int | None):
                Timeout in seconds, default is 60 seconds.

        Raises:
            TimeoutError: thrown when the time limit is exceeded.
        """
        if not issubclass(type, Update):
            raise TypeError(f'Type {type} is not an update type.')

        # Getting the pendencies list.
        pendencies = self.dispatcher.pendencies

        # Creating a pendency.
        pendency = dict(
            # NOTE: the dispatcher will set the value of the `update` key.
            update=None,
            filter=filter,
            type=type
        )

        # Adding the pendency to pendencies list.
        pendencies.append(pendency)

        # Getting current time to calculate execution time.
        before_time = time.time()

        # While the pendency does not receive a update.
        while pendency['update'] is None:
            # If the time limit has been exceeded.
            if timeout is not None and time.time() - before_time >= timeout:
                # Removing the pendency from pendencies list.
                pendencies.remove(pendency)

                # Thrown TimeoutError exception.
                raise TimeoutError('timeout reached.')

            # HACK: This line is only for the concurrency
            # exchange to be performed and to prevent the
            # while from blocking the execution of the event loop.
            await asyncio.sleep(0)

        # Removing the pendency from pendencies list.
        pendencies.remove(pendency)

        # Returns the update received by dispatcher.
        return pendency['update']
