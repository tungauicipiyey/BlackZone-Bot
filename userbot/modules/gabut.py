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
    await pong.edit("**γβππππππγ**")
    await pong.edit("**ββπππππππββ**")
    await pong.edit("**ππππππππ ππππ πππ πππ**")
    await pong.edit("**β¬ππππ πππππππ ππππππππ πππβ¬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**β² πΊπΎπ½ππΎπ» πΌπ΄π»π΄π³ππΆ** "
                    f"\n β«Έ α΄·α΅βΏα΅α΅Λ‘ `%sms` \n"
                    f"**β² π±πΈπΉπΈ πΏπ΄π»π΄π** "

                    f"\n β«Έ α΄·α΅α΅α΅α΅βΏα΅γ`{ALIVE_NAME}`γ \n" % (duration))


@register(outgoing=True, pattern='^.kar(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**πππ«π’π§π ππ’π­ππ§π’π πππ₯π¬πππ’π₯ππ**")
    sleep(1)
    await typew.edit("**Bidadari Bali β**")
    await typew.edit("**Bidadari Bali β**")
    sleep(1)
    await typew.edit("**Capricorn Girl β¨β**")
    await typew.edit("**Capricorn Girl β¨β**")
    sleep(1)
    await typew.edit("**15 Years Old πβ**")
    await typew.edit("**15 Years Old πβ**")
    sleep(1)
    await typew.edit("**Favorite Girl πβ**")
    await typew.edit("**Favorite Girl πβ**")
    sleep(1)
    await typew.edit("**Cuteee Girll πΈβ**")
    await typew.edit("**Cuteee Girll πΈβ**")
    sleep(1)
    await typew.edit("**Seringg Lemot Tapi Lucu π»β**")
    await typew.edit("**Seringg Lemot Tapi Lucu π»β**")
    sleep(1)
    await typew.edit("**Kadang Ngeselin β**")
    await typew.edit("**Kadang Ngeselin β**")
    sleep(1)
    await typew.edit("**And Call Me Karina π**")
    sleep(1)
    await typew.edit("**Thankss All ππ**")
    sleep(1)
    await typew.edit("**I Love Youu πβ**")
    await typew.edit("**I Love Youu πβ**")


@register(outgoing=True, pattern='^.cabean(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Pasukan Cabe Cabean π¦π¦**")
    sleep(1)
    await typew.edit(f"**Adel Sangeeann β**")
    await typew.edit(f"**Adel Sangeeann β**")
    sleep(1)
    await typew.edit(f"**Jia Partner Sangean Adel β**")
    await typew.edit(f"**Jia Partner Sangean Adel β**")
    sleep(1)
    await typew.edit(f"**Jeje Ratu Colmekk β**")
    await typew.edit(f"**Jeje Ratu Colmekk β**")
    sleep(1)
    await typew.edit(f"**Imeh Ratu Desahh β**")
    await typew.edit(f"**Imeh Ratu Desahh β**")
    sleep(1)
    await typew.edit(f"**Karina Cewe Penggoda β**")
    await typew.edit(f"**Karina Cewe Penggoda β**")
    sleep(1)
    await typew.edit(f"**Tata Partner Desahh Imeh β**")
    await typew.edit(f"**Tata Partner Desahh Imeh β**")
    sleep(1)
    await typew.edit(f"**Pasukan Cabe Cabean Ready β**")
    await typew.edit(f"**Pasukan Cabe Cabean Ready β**")


@register(outgoing=True, pattern='^.intro(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii,Saya Tungauuπ..**")
    sleep(1)
    await typew.edit("**Askot Pekanbaruπ..**")
    sleep(1)
    await typew.edit("**Saya BerUsia 18 Tahunπ..**")
    sleep(1)
    await typew.edit("**Salam Kenal Ya,Terimakasih π..**")
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
    await typew.edit("**PASUKANN SAGAPUNGG π¦π¦**")
    sleep(1)
    await typew.edit(f"**Alvin Korban Gay β**")
    await typew.edit(f"**Alvin Korban Gay β**")
    sleep(1)
    await typew.edit("**Friski Kang Coli β π¦**")
    await typew.edit("**Friski Kang Coli β π¦**")
    sleep(1)
    await typew.edit("**Toni Partner Gay Alvin β**")
    await typew.edit("**Toni Partner Gay Alvinβ**")
    sleep(1)
    await typew.edit("**Tungau Ketua Sagapung β π¦...**")
    await typew.edit("**Tungau Ketua Sagapung β π¦...**")
    sleep(1)
    await typew.edit("**Rama Sangeann β π¦..**")
    await typew.edit("**Rama Sangeann β π¦..**")
    sleep(1)
    await typew.edit("**Hendra Kang Tusbooll β ..**")
    await typew.edit("**Hendra Kang Tusbooll β ..**")
    sleep(1)
    await typew.edit("**PASUKANN SAGAPUNGG READYY β πππ¦**")
    await typew.edit("**PASUKANN SAGAPUNGG READYY β πππ¦**")

# Owner @Si_Dian


@register(outgoing=True, pattern='^.usange(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("γ€**β­βΌβββββββββββββββββΎβ?**\n**βγ€γ€γ€βπππππ π½ππ πΏπππβγ€γ€β¨γ**\nγ€**β°βΌβββββββββββββββββΎβ―**\n**ββββββββββββΉβββββββββββ**\n" f"**β’ `Penggunaan Sperma ` {ALIVE_NAME}**\n" f" β₯**0 jam - " f"0 menit - 0%**" "\n  **β°β±β°β±β°β±β°β±β°β±β°β±β°β±β°** \n" "**β’ `Sisa Sperma Bulan Ini` **\n" f" β₯**9999 jam - 9999 menit " f"- 100%**\n**ββββββββββββΉβββββββββββ**"
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
