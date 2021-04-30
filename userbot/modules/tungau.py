# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD
""" Userbot module for other small commands. """

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
import urllib


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

opener = urllib.request.build_opener()
useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36'
opener.addheaders = [('User-agent', useragent)]


@register(outgoing=True, pattern="^.ainna$")
async def repo_is_here(wannasee):
    """ For .ainna command, just returns the ainna URL. """
    await wannase.edit(
        " **INSTAGRAM: ** [KLICK FOR MY INSTAGRAM AINNA](https: // www.instagram.com/ainnaaa.yr)"
    )


CMD_HELP.update({
    "random":
    ">`.ainna\
    \nUsage: Link Url Instagram.",
})
