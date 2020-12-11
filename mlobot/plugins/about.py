# Ported from other Telegram UserBots for Mlobot//Made for MloBot
# Kangers, don't remove this line
# @its_xditya

"""Available Commands:
.info
"""

import asyncio

from mlobot import CMD_HELP


@mlobot.on(admin_cmd(pattern="info"))
@mlobot.on(sudo_cmd(pattern="info", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Visit this page to know more about TeleBot.":
    await eor(event, "Thanks")
    animation_chars = ["**Mlobot**"

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await eor(event, animation_chars[i % 18])


CMD_HELP.update({"about": "➟ .info\nUse - Get to know about your bot."})
