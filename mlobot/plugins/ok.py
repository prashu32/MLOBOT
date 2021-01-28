# PLUGINS FOR MLOBOT BY @MBBS_LOVER

"""Emoji
Available Commands:
.ok"""


import asyncio

from mlobot.utils import admin_cmd


@mlobot.on(admin_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.00001
    animation_ttl = range(0, 90)
    input_str = event.pattern_match.group(1)
    if input_str == "ok":
        await event.edit(input_str)
        animation_chars = [
            "O",
            "Y",
            "E",
            "S",
            "U",
            "N",
            "U",
            "B",
            "C",
            "FK",
            "UU",
            "GAND",
            "MAR",
            "L",
            "U",
            "N",
            "G",
            "A",
            "Ok bhosri wale Sar mlo SE panga nhi😇",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 18])
