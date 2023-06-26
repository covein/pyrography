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
import logging
import signal
from signal import signal as signal_fn, SIGINT, SIGTERM, SIGABRT
import threading

log = logging.getLogger(__name__)

# Signal number to name
signals = {
    k: v for v, k in signal.__dict__.items()
    if v.startswith("SIG") and not v.startswith("SIG_")
}


# FIXME: Have some possible code improvement?
def create_thread(function):
    def inner(*args, **kwargs):
        threading.Thread(
            target=function,
            args=args,
            kwargs=kwargs
        ).start()
    return inner


def set_interruption_signal_handlers(handler):
    for s in (SIGINT, SIGTERM, SIGABRT):
        signal_fn(s, create_thread(handler))


async def idle(client):
    """Block the main script execution until a signal is received.

    This function will run indefinitely in order to block the main script execution and prevent it from
    exiting while having client(s) that are still running in the background.

    It is useful for event-driven application only, that are, applications which react upon incoming Telegram
    updates through handlers, rather than executing a set of methods sequentially.

    Once a signal is received (e.g.: from CTRL+C) the function will terminate and your main script will continue.
    Don't forget to call :meth:`~pyrography.Client.stop` for each running client before the script ends.

    Example:
        .. code-block:: python

            import asyncio
            from pyrography import Client, idle


            async def main():
                apps = [
                    Client("account1"),
                    Client("account2"),
                    Client("account3")
                ]

                ...  # Set up handlers

                for app in apps:
                    await app.start()

                await idle(Client)

                for app in apps:
                    await app.stop()


            asyncio.run(main())
    """
    task = None
    signalized = False

    def signal_handler(signum, __):
        # Accessing nonlocal variable.
        nonlocal signalized

        # Prevent unnecessary execution.
        if signalized:
            return

        # Set as signalized.
        signalized = True

        logging.info(
            f"Stop signal received ({signals[signum]}). Preparing to stop..."
        )

        dispatcher = client.dispatcher

        # Removing all registered handlers to prevent new tasks.
        logging.info('Removing all registered handlers to prevent new tasks.')
        dispatcher.groups.clear()

        # Waiting for running handlers to terminate.
        logging.info('Waiting for running handlers to terminate..')
        while dispatcher.running_handlers:
            pass

        # If there are pendencies.
        if dispatcher.pendencies:
            logging.info((
                '{} pendencies waiting for resolution, '
                'you must to wait it.'
            ).format(len(dispatcher.pendencies)))

        # Waiting the pendencies resolution.
        while dispatcher.pendencies:
            pass

        # Stop listening.
        task.cancel()

    # Setting all interrupting signals with a custom handler.
    set_interruption_signal_handlers(
        create_thread(signal_handler)
    )

    while True:
        task = asyncio.create_task(asyncio.sleep(600))

        try:
            await task
        except asyncio.CancelledError:
            break
