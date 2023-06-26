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

import logging
from typing import Union

import pyrography
from pyrography import raw

log = logging.getLogger(__name__)


class GetChatHistoryCount:
    async def get_chat_history_count(
        self: "pyrography.Client",
        chat_id: Union[int, str]
    ) -> int:
        """Get the total count of messages in a chat.

        .. note::

            Due to Telegram latest internal changes, the server can't reliably find anymore the total count of messages
            a **private** or a **basic group** chat has with a single method call. To overcome this limitation, Pyrogram
            has to iterate over all the messages. Channels and supergroups are not affected by this limitation.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``int``: On success, the chat history count is returned.

        Example:
            .. code-block:: python

                await app.get_history_count(chat_id)
        """

        r = await self.invoke(
            raw.functions.messages.GetHistory(
                peer=await self.resolve_peer(chat_id),
                offset_id=0,
                offset_date=0,
                add_offset=0,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0
            )
        )

        if isinstance(r, raw.types.messages.Messages):
            return len(r.messages)
        else:
            return r.count
