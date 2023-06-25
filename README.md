<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://github.com/d3cryptofc/pyrography/assets/47941854/0eb90a78-5054-497e-8c86-b5f6bbb70822" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br/>A wonderful Pyrogram fork inspired by Pyromod & AmanoTeam/Pyrogram
    <br>
    <a href="https://pyrogram.org">
        Homepage
    </a>
    •
    <a href="https://docs.pyrogram.org">
        Documentation
    </a>
    •
    <a href="https://docs.pyrogram.org/releases">
        Releases
    </a>
    •
    <a href="https://t.me/pyrogram">
        News
    </a>
</p>

## Pyrography

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

```python3
import asyncio
from pyrography import Client, filters, idle

# Creating a client instance to control your bot.
# NOTE: Get your `api_id` and `api_hash` credentials on: my.telegram.org
client = Client(
    name='your_session_name',
    api_id=...,
    api_hash=...
)


@client.on_message(filters.command('start'))
async def ask_user_name(client, message):
    # Ask the user age.
    asking = message.ask("What's your name?")

    # Getting ask message and answer message.
    # TIP: you can to use `async for` too!
    ask, answer = await anext(asking)

    # Getting message text.
    user_name = answer.text

    # Replying message.
    await answer.reply(f'Nice name, {user_name}!')


async def main():
    # Start MTProto connection.
    await client.start()

    # Listen all command handlers.
    await idle(client)

    # When idle() is terminated, stop the client.
    await client.stop()

if __name__ == '__main__':
    # Getting asyncio event loop.
    loop = asyncio.get_event_loop()

    # Run main() function until complete it.
    loop.run_until_complete(main())
```

**Pyrography** is a modern, elegant and asynchronous [MTProto API](https://docs.pyrogram.org/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

#### Why should you use Pyrography?

##### 1. Stop safety
Pyrography is the only mtproto library currently that when pressing `CTRL + C` to interrupt the program, it will wait for pending commands to finish, preventing anything from being incomplete.

#### To most performance and others

##### [TgCrypto](https://pypi.org/project/TgCrypto/)
A Cryptography Library written in C as a Python extension. It is designed to be portable, fast, easy to install and use. TgCrypto is intended for Pyrogram and implements the cryptographic algorithms Telegram requires.

Automatically installed, ignore it.

##### [Uvloop](https://pypi.org/project/uvloop/)
A fast, drop-in replacement of the built-in asyncio event loop. uvloop is implemented in Cython and uses libuv under the hood.

Install it with `pip install uvloop`, import it and call `uvloop.install()` in your main script.

##### Latency
On hosting, choose an region close to Miami to your machine.

##### Wonderful logging
Use the `rich` library to have pretty logs.

Automatically installed and default setted on `log_level` client parameter, set with `logging.NOTSET` to disable it.

```python3
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler()]
)

log = logging.getLogger(__name__)
log.info("Hello, World!")
```

[Read more here](https://rich.readthedocs.io/en/stable/logging.html).

### Installing

#### Pypi

```
pip install pyrography
```

#### Github

```
pip3 install git+https://github.com/d3cryptofc/pyrography
```

### Support Official Pyrogram

If you'd like to support the official Pyrogram, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/delivrance).
- [Become a LiberaPay patron](https://liberapay.com/delivrance).
- [Become an OpenCollective backer](https://opencollective.com/pyrogram).

### Resources

- Check out the docs at https://docs.pyrogram.org to learn more about Pyrogram, get started right
away and discover more in-depth material for building your client applications.
- Join the official channel at https://t.me/pyrogram and stay tuned for news, updates and announcements.
