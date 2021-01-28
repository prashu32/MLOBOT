import asyncio
import os
from asyncio import sleep

from telegraph import Telegraph, upload_file

from mlobot.mlobotConfig import Config

from .. import CMD_HELP

#############-CONSTANTS-###############
LOGGER_GROUP = Var.PRIVATE_GROUP_ID
LOGGER = True
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]
#######################################

# ported by @MBBS_LOVER


@mlobot.on(admin_cmd(pattern="tspam"))
@mlobot.on(sudo_cmd(pattern="tspam", allow_sudo=True))
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()


@mlobot.on(admin_cmd(pattern="spam"))
@mlobot.on(sudo_cmd(pattern="spam", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@mlobot.on(admin_cmd(pattern="bigspam"))
@mlobot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@mlobot.on(admin_cmd(pattern="picspam"))
@mlobot.on(sudo_cmd(pattern="picspam", allow_sudo=True))
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        r_message = await e.get_reply_message()
        downloaded_file_name = await borg.download_media(
            r_message, Config.TMP_DOWNLOAD_DIRECTORY
        )
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            x = upload_file(downloaded_file_name)
            url = f"https://telegra.ph/{x[0]}"
            os.remove(downloaded_file_name)
        except BaseException:
            return await e.edit("Error!")
        if url:
            for i in range(1, counter):
                await e.client.send_file(e.chat_id, url)
            await e.delete()
        else:
            await e.edit("Pic not supported :/")
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#PICSPAM \n\n" "PicSpam was executed successfully"
            )


@mlobot.on(admin_cmd(pattern="delayspam (.*)"))
@mlobot.on(sudo_cmd(pattern="delayspam (.*), allow_sudo=True"))
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(" ", 2)[0])
    counter = int(e.pattern_match.group(1).split(" ", 2)[1])
    spam_message = str(e.pattern_match.group(1).split(" ", 2)[2])
    await e.delete()
    for i in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if LOGGER:
        await e.client.send_message(
            LOGGER_GROUP, "#DelaySPAM\n" "DelaySpam was executed successfully"
        )


CMD_HELP.update(
    {
        "spam": ".tspam <sentence>\nUse - Text spam\
        \n\n.spam <number> <sentence>\nUse - Spam\
        \n\n.bigspam <number> <sentence>\nUse - Bigger Spam\
        \n\n.picspam <reply to pic> <number>\nUse - Picture Spam\
        \n\n.delayspam <time> <word>\nUse - Spam, with some time delay!"
    }
)
