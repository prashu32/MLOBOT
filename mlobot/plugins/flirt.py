# Coded by @MysteryxD and @the_legend16 for Mystery Userbot
# Don't Remove these credits. Else you will be gayest gay and of course noobest noob.

import asyncio
import random

from mlobot import CMD_HELP
from mlobot.utils import admin_cmd


@mlobot(admin_cmd(pattern=r"flirt$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Here's a **special** fact about you......")
    await asyncio.sleep(1)
    s = random.randrange(1, 8)
    if s == 1:
        await event.edit(
            "Do you have an inhaler? Because you took my breath away!!"
        )
    if s == 2:
        await event.edit(
            "As she’s leaving….Hey aren’t you forgetting something? She: What? Me!"
        )
    if s == 3:
        await event.edit(
            "I want to be your tear drop, so I could be born in your eyes, live on your cheeks, and die on your lips."
        )
    if s == 4:
        await event.edit(
            "There isn’t a word in the dictionary to describe how beautiful you are."
        )
    if s == 5:
        await event.edit("You look cold. Want to use me as a blanket?")
    if s == 6:
        await event.edit(
            "Do you have a band aid? Cause I scrapped my knees falling for you."
        )
    if s == 7:
        await event.edit("Of all your beautiful curves, your smile is my favourite.")
    if s == 8:
        await event.edit(
            "There’s only one thing I want to change about you. Your last name."
        )
    if s == 9:
        await event.edit("I’m no organ donor but I’d be happy to give you my heart.")
    if s == 10:
        await event.edit("Is Your Dad A Preacher? Cause Girl You’re A Blessing.")
    if s == 11:
        await event.edit(
            "Can you touch me? I want to tell my friends I was touched by an Angel."
        )
    if s == 12:
        await event.edit(
            "Did you die recently? Cause girl, you look like an angel to me."
        )
    if s == 13:
        await event.edit("If I was an octopus, all my 3 hearts would beat for you﻿.")
    if s == 14:
        await event.edit(
            "I should call you Google, because you have everything I’m looking for."
        )
    if s == 15:
        await event.edit("Can I follow you? Cause my mom told me to follow my dreams.")
    if s == 16:
        await event.edit("Guess what I’m wearing? The smile you gave me!")
    if s == 17:
        await event.edit(
            "Roses are red, my face is too, that only happens when I’m around you."
        )
    if s == 18:
        await event.edit("Are you McDonald’s? Cause I’m loving it!")
    if s == 19:
        await event.edit(
            "Do you know if there are any police around? Cause I’m about to steal your heart."
        )
    if s == 20:
        await event.edit("Are you netflix? Because i could watch you for hours.")
    if s == 21:
        await event.edit("Your lips look lonely would they like to meet mine?")
    if s == 22:
        await event.edit(
            "I’d never play hide and seek with you because someone like you is impossible to find."
        )
    if s == 23:
        await event.edit("Are you a keyboard? Because you’re just my type.")
    if s == 24:
        await event.edit(
            "Are you the cure for Alzheimer’s? Because you’re unforgettable."
        )
    if s == 25:
        await event.edit("Do you play soccer? Because you’re a keeper!")
    if s == 26:
        await event.edit("Are you a time traveler? Cause I see you in my future!")
    if s == 27:
        await event.edit("I’m not electrician, but I can light up your day.")
    if s == 28:
        await event.edit("Are you a bank loan? Because you got my interest.")
    if s == 29:
        await event.edit(
            "See my friend over there? He wants to know if you think I’m cute."
        )
    if s == 30:
        await event.edit(
            "Hey, tie your shoes! I don’t want you falling for anyone else."
        )
    if s == 31:
        await event.edit("Your hand looks heavy can I hold it for you?")
    if s == 32:
        await event.edit(
            "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together"
        )
    if s == 33:
        await event.edit("If you were a sea i would swim in you forever.")
    if s == 34:
        await event.edit("My love for you is like dividing by zero. It’s undefinable.")
    if s == 35:
        await event.edit(
            "Are you a magician? Because whenever I look at you everyone else disappears."
        )
    if s == 36:
        await event.edit(
            "Give me your photo. I want to show my mom what my next girlfriend looks like."
        )
    if s == 37:
        await event.edit(
            "There must be something wrong with my eyes, I can’t take them off you."
        )
    if s == 38:
        await event.edit("See these keys? I wish I had the one to your heart.")
    if s == 39:
        await event.edit("Life without you would be like a broken pencil… pointless.")
    if s == 40:
        await event.edit("Is it hot in here or is it just you?")
    if s == 41:
        await event.edit(
            "What are you doing for the rest of your life? Because I want to spend it with you."
        )
    if s == 42:
        await event.edit("Did it hurt? When you fell from heaven.")
    if s == 43:
        await event.edit("Are you an oven? Because damn you are hot :D")


CMD_HELP.update({"flirt": ".flirt\nUse - Flirting / Pickup lines in english."})
