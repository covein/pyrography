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

from uuid import uuid4

import pyrography
from pyrography import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~pyrography.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrography.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrography.types.InlineQueryResultCachedAnimation`
    - :obj:`~pyrography.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrography.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrography.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrography.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrography.types.InlineQueryResultArticle`
    - :obj:`~pyrography.types.InlineQueryResultAudio`
    - :obj:`~pyrography.types.InlineQueryResultContact`
    - :obj:`~pyrography.types.InlineQueryResultDocument`
    - :obj:`~pyrography.types.InlineQueryResultAnimation`
    - :obj:`~pyrography.types.InlineQueryResultLocation`
    - :obj:`~pyrography.types.InlineQueryResultPhoto`
    - :obj:`~pyrography.types.InlineQueryResultVenue`
    - :obj:`~pyrography.types.InlineQueryResultVideo`
    - :obj:`~pyrography.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyrography.Client"):
        pass
