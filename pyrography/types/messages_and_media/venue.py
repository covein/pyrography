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

import pyrography
from pyrography import raw
from pyrography import types
from ..object import Object


class Venue(Object):
    """A venue.

    Parameters:
        location (:obj:`~pyrography.types.Location`):
            Venue location.

        title (``str``):
            Name of the venue.

        address (``str``):
            Address of the venue.

        foursquare_id (``str``, *optional*):
            Foursquare identifier of the venue.

        foursquare_type (``str``, *optional*):
            Foursquare type of the venue.
            (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)

    """

    def __init__(
        self,
        *,
        client: "pyrography.Client" = None,
        location: "types.Location",
        title: str,
        address: str,
        foursquare_id: str = None,
        foursquare_type: str = None
    ):
        super().__init__(client)

        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type

    @staticmethod
    def _parse(client, venue: "raw.types.MessageMediaVenue"):
        return Venue(
            location=types.Location._parse(client, venue.geo),
            title=venue.title,
            address=venue.address,
            foursquare_id=venue.venue_id or None,
            foursquare_type=venue.venue_type,
            client=client
        )
