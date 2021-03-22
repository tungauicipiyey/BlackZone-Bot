from datetime import datetime
import time
from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.keping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await pong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await pong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await pong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
                    f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
                    f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "

                    f"\n ⫸ ᴷᵃᵐᵖᵃⁿᵍ『`{ALIVE_NAME}`』 \n" % (duration))


@register(outgoing=True, pattern='^.kar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**𝐊𝐚𝐫𝐢𝐧𝐚 𝐓𝐢𝐭𝐚𝐧𝐢𝐚 𝐒𝐚𝐥𝐬𝐚𝐛𝐢𝐥𝐚💛**")
    sleep(1)
    await typew.edit("**Bidadari Bali ☑**")
    await typew.edit("**Bidadari Bali ✅**")
    sleep(1)
    await typew.edit("**Capricorn Girl ✨☑**")
    await typew.edit("**Capricorn Girl ✨✅**")
    sleep(1)
    await typew.edit("**15 Years Old 💛☑**")
    await typew.edit("**15 Years Old 💛✅**")
    sleep(1)
    await typew.edit("**Favorite Girl 💛☑**")
    await typew.edit("**Favorite Girl 💛✅**")
    sleep(1)
    await typew.edit("**Cuteee Girll 🌸☑**")
    await typew.edit("**Cuteee Girll 🌸✅**")
    sleep(1)
    await typew.edit("**Seringg Lemot Tapi Lucu 👻☑**")
    await typew.edit("**Seringg Lemot Tapi Lucu 👻✅**")
    sleep(1)
    await typew.edit("**Kadang Ngeselin ☑**")
    await typew.edit("**Kadang Ngeselin ✅**")
    sleep(1)
    await typew.edit("**And Call Me Karina 💛**")
    sleep(1)
    await typew.edit("**Thankss All 🙏💛**")
    sleep(1)
    await typew.edit("**I Love Youu 💛☑**")
    await typew.edit("**I Love Youu 💛✅**")


@register(outgoing=True, pattern='^.cabean(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Pasukan Cabe Cabean 💦💦**")
    sleep(1)
    await typew.edit(f"**Adel Sangeeann ☑**")
    await typew.edit(f"**Adel Sangeeann ✅**")
    sleep(1)
    await typew.edit(f"**Jia Partner Sangean Adel ☑**")
    await typew.edit(f"**Jia Partner Sangean Adel ✅**")
    sleep(1)
    await typew.edit(f"**Jeje Ratu Colmekk ☑**")
    await typew.edit(f"**Jeje Ratu Colmekk ✅**")
    sleep(1)
    await typew.edit(f"**Imeh Ratu Desahh ☑**")
    await typew.edit(f"**Imeh Ratu Desahh ✅**")
    sleep(1)
    await typew.edit(f"**Karina Cewe Penggoda ☑**")
    await typew.edit(f"**Karina Cewe Penggoda ✅**")
    sleep(1)
    await typew.edit(f"**Tata Partner Desahh Imeh ☑**")
    await typew.edit(f"**Tata Partner Desahh Imeh ✅**")
    sleep(1)
    await typew.edit(f"**Pasukan Cabe Cabean Ready ☑**")
    await typew.edit(f"**Pasukan Cabe Cabean Ready ✅**")


@register(outgoing=True, pattern='^.intro(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii,Saya Tungauu👋..**")
    sleep(1)
    await typew.edit("**Askot Pekanbaru😇..**")
    sleep(1)
    await typew.edit("**Saya BerUsia 18 Tahun😇..**")
    sleep(1)
    await typew.edit("**Salam Kenal Ya,Terimakasih 🙏..**")
# Owner @Si_Dian


@register(outgoing=True, pattern='^ass(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Assalamu'alaikum Babu..`")
# Owner @mixiologist


@register(outgoing=True, pattern='^.sagapung(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**PASUKANN SAGAPUNGG 💦💦**")
    sleep(1)
    await typew.edit(f"**Alvin Korban Gay ☑**")
    await typew.edit(f"**Alvin Korban Gay ✅**")
    sleep(1)
    await typew.edit("**Friski Kang Coli ☑ 💦**")
    await typew.edit("**Friski Kang Coli ✅ 💦**")
    sleep(1)
    await typew.edit("**Toni Partner Gay Alvin ☑**")
    await typew.edit("**Toni Partner Gay Alvin✅**")
    sleep(1)
    await typew.edit("**Tungau Ketua Sagapung ☑ 💦...**")
    await typew.edit("**Tungau Ketua Sagapung ✅ 💦...**")
    sleep(1)
    await typew.edit("**Rama Sangeann ☑ 💦..**")
    await typew.edit("**Rama Sangeann ✅ 💦..**")
    sleep(1)
    await typew.edit("**Hendra Kang Tusbooll ☑ ..**")
    await typew.edit("**Hendra Kang Tusbooll ✅ ..**")
    sleep(1)
    await typew.edit("**PASUKANN SAGAPUNGG READYY ☑ 👉👌💦**")
    await typew.edit("**PASUKANN SAGAPUNGG READYY ✅ 👉👌💦**")

# Owner @Si_Dian


@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**╭╼════════════════╾╮**\n**⊏ㅤㅤ≛𝙑𝙄𝙍𝙐𝙎 𝘽𝙊𝙏 𝘿𝙔𝙉𝙊≛ㅤㅤ⊨〛**\n**╰╼════════════════╾╯**\n" f"⌲** `Penggunaan Sperma ` {ALIVE_NAME}**\n" f" ➥**0 jam - " f"0 menit - 0%**" "\n  **▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰** \n" "⌲** `Sisa Sperma Bulan Ini` **\n" f" ➥**9999 jam - 9999 menit " f"- 100%**\n"
                     )
# @mixiologist


CMD_HELP.update({
    "virus":
    "`.usange`\
\nUsage: tipu tipu anjeeeng.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam.\
\n\n`.sagapung`\
\nUsage: liat aja anak anak tolol.\
\n\n`.kar`\
\nUsage: my favorit girl.\
\n\n`ass`\
\nUsage: melakukan salam.\
\n\n`.cabean`\
\nUsage: liat aja anak anak tolol.\
\n\n`.keping`\
\nUsage: liat keceptan ping."
})
