from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

# -ل

sython1.start()
sython2.start()
sython3.start()
sython4.start()
sython5.start()


c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5568351247]




@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
      

@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass  
        
        
@sython2.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython2(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
        
@sython2.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython2(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
      

@sython2.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython2(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass  
        
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
        
@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
      

@sython3.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython3(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass  
        
        
@sython4.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython4(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
        
@sython4.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython4(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass
      

@sython4.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython4(JoinChannelRequest("@kl_ok1"))
    except BaseException:
        pass  
        
        
@sython5.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython5(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@sython5.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython5(JoinChannelRequest("@xx1x1xx"))
    except BaseException:
        pass
      

@sython5.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython5(JoinChannelRequest("@xx1x1xx"))
    except BaseException:
        pass  
        
        

        
        
        
        
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/Al'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**✅اداه تعمل بشكل جيد ارسل امر تجميع نقاط للبد**')

@sython2.on(events.NewMessage(outgoing=False, pattern='/Al'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**✅اداه تعمل بشكل جيد ارسل امر تجميع نقاط للبد**')


@sython3.on(events.NewMessage(outgoing=False, pattern='/Al'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**✅اداه تعمل بشكل جيد ارسل امر تجميع نقاط للبد**')


@sython4.on(events.NewMessage(outgoing=False, pattern='/Al'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**✅اداه تعمل بشكل جيد ارسل امر تجميع نقاط للبد**')

@sython5.on(events.NewMessage(outgoing=False, pattern='/Al'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**✅اداه تعمل بشكل جيد ارسل امر تجميع نقاط للبد**')

@sython1.on(events.NewMessage(outgoing=False, pattern='/ss'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/Bl`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")

@sython2.on(events.NewMessage(outgoing=False, pattern='/ss'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/Bl`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")

@sython3.on(events.NewMessage(outgoing=False, pattern='/ss'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/Bl`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")


@sython4.on(events.NewMessage(outgoing=False, pattern='/ss'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/Bl`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")

@sython5.on(events.NewMessage(outgoing=False, pattern='/ss'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/Bl`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")





@sython1.on(events.NewMessage(outgoing=True, pattern="/ss"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@sython2.on(events.NewMessage(outgoing=True, pattern="/ss"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@sython3.on(events.NewMessage(outgoing=True, pattern="/ss"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@sython4.on(events.NewMessage(outgoing=True, pattern="./ss"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@sython5.on(events.NewMessage(outgoing=True, pattern="/ss"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")

@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''✅سورس يعمل بشكل جيد ''')

@sython1.on(events.NewMessage(outgoing=False, pattern='/BL'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_username)
    await sython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernamee)
    await sython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameee)
    await sython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameeee)
    await sython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_username)
    await sython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernamee)
    await sython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameee)
    await sython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameeee)
    await sython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):

    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''✅سورس يعمل بشكل جيد''')

@sython2.on(events.NewMessage(outgoing=False, pattern='/Bl'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_username)
    await sython2.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython2.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_usernamee)
    await sython2.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython2.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_usernameee)
    await sython2.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython2.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_usernameeee)
    await sython2.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython2.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_username)
    await sython2.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython2.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_usernamee)
    await sython2.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython2.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_usernameee)
    await sython2.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython2.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython2(JoinChannelRequest('saythonh'))
    channel_entity = await sython2.get_entity(bot_usernameeee)
    await sython2.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython2.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython2(ImportChatInviteRequest(bott))
            msg2 = await sython2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython2.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython3.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
	
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''✅سورس يعمل بشكل جيد''')

@sython3.on(events.NewMessage(outgoing=False, pattern='/Bl'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_username)
    await sython3.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython3.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_usernamee)
    await sython3.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython3.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_usernameee)
    await sython3.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython3.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_usernameeee)
    await sython3.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython3.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_username)
    await sython3.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython3.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_usernamee)
    await sython3.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython3.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_usernameee)
    await sython3.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython3.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython3(JoinChannelRequest('saythonh'))
    channel_entity = await sython3.get_entity(bot_usernameeee)
    await sython3.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython3.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython3(ImportChatInviteRequest(bott))
            msg2 = await sython3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython3.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython4.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
	
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''✅سورس يعمل بشكل جيد''')

@sython4.on(events.NewMessage(outgoing=False, pattern='/Bl'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_username)
    await sython4.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython4.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_usernamee)
    await sython4.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython4.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_usernameee)
    await sython4.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython4.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_usernameeee)
    await sython4.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython4.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_username)
    await sython4.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython4.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_usernamee)
    await sython4.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython4.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_usernameee)
    await sython4.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython4.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython4(JoinChannelRequest('saythonh'))
    channel_entity = await sython4.get_entity(bot_usernameeee)
    await sython4.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython4.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython4(ImportChatInviteRequest(bott))
            msg2 = await sython4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython4.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython5.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
	
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''✅سورس يعمل بشكل جيد''')

@sython5.on(events.NewMessage(outgoing=False, pattern='/Bl'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_username)
    await sython5.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython5.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_usernamee)
    await sython5.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython5.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_usernameee)
    await sython5.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython5.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_usernameeee)
    await sython5.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython5.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_username)
    await sython5.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython5.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_usernamee)
    await sython5.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython5.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_usernameee)
    await sython5.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython5.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython5(JoinChannelRequest('saythonh'))
    channel_entity = await sython5.get_entity(bot_usernameeee)
    await sython5.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython5.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython5(ImportChatInviteRequest(bott))
            msg2 = await sython5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython5.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")




@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_username, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await sython1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@sython2.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython2.send_message(bot_username, pt)
    sleep(4)
    msg = await sython2.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython2.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython2.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython2.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython2.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython2.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython2.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython2.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython2.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython2.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython2.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython2.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython2.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython2.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython2.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython2.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython2.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython2.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython2.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython2.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await sython2(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@sython3.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython3.send_message(bot_username, pt)
    sleep(4)
    msg = await sython3.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython3.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython3.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython3.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython3.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython3.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython3.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython3.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython3.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython3.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython3.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython3.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython3.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython3.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython3.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython3.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython3.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython3.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython3.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython3.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await sython3(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@sython4.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython4.send_message(bot_username, pt)
    sleep(4)
    msg = await sython4.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython4.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython4.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython4.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython4.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython4.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython4.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython4.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython4.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython4.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython4.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython4.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython4.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython4.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython4.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython4.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython4.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython4.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython4.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython4.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await sython4(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@sython5.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython5.send_message(bot_username, pt)
    sleep(4)
    msg = await sython5.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython5.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython5.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await sython5.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@sython5.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython5.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await sython5.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython5.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await sython5.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await sython5.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython5.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython5.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython5.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython5.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@sython5.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython5.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@sython5.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await sython5.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@sython5.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await sython5.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await sython5(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
       

@sython1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    
@sython2.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython2.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
@sython3.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython3.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**") 

@sython4.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython4.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**") 

@sython5.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython5.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**") 


@sython1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")

@sython2.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")

@sython3.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")


@sython4.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")

@sython5.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")


@sython1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@sython2.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@sython3.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@sython4.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@sython5.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@sython1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await sython1.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@sython1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await sython1(JoinChannelRequest('d3boot_7'))
        joinw = await sython1(JoinChannelRequest('Fvvvv'))
        joine = await sython1(JoinChannelRequest('DzDDDD'))
        joinr = await sython1(JoinChannelRequest('botbillion'))
        joint = await sython1(JoinChannelRequest('zzzzzz1'))
        joiny = await sython1(JoinChannelRequest('zzzzzz'))

        joini = await sython1(JoinChannelRequest('zz_MX'))
        joino = await sython1(JoinChannelRequest('zd_e6'))
        joinp = await sython1(JoinChannelRequest('KTTTT'))
        joina = await sython1(JoinChannelRequest('RRXFR'))
        sendd = await sython1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@sython2.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython2.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython2.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@sython2.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await sython2.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@sython2.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython2.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await sython2(JoinChannelRequest('d3boot_7'))
        joinw = await sython2(JoinChannelRequest('Fvvvv'))
        joine = await sython2(JoinChannelRequest('DzDDDD'))
        joinr = await sython2(JoinChannelRequest('botbillion'))
        joint = await sython2(JoinChannelRequest('zzzzzz1'))
        joiny = await sython2(JoinChannelRequest('zzzzzz'))

        joini = await sython2(JoinChannelRequest('zz_MX'))
        joino = await sython2(JoinChannelRequest('zd_e6'))
        joinp = await sython2(JoinChannelRequest('KTTTT'))
        joina = await sython2(JoinChannelRequest('RRXFR'))
        sendd = await sython2.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@sython3.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython3.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython3.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@sython3.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await sython3.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@sython3.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython3.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await sython3(JoinChannelRequest('d3boot_7'))
        joinw = await sython3(JoinChannelRequest('Fvvvv'))
        joine = await sython3(JoinChannelRequest('DzDDDD'))
        joinr = await sython3(JoinChannelRequest('botbillion'))
        joint = await sython3(JoinChannelRequest('zzzzzz1'))
        joiny = await sython3(JoinChannelRequest('zzzzzz'))

        joini = await sython3(JoinChannelRequest('zz_MX'))
        joino = await sython3(JoinChannelRequest('zd_e6'))
        joinp = await sython3(JoinChannelRequest('KTTTT'))
        joina = await sython3(JoinChannelRequest('RRXFR'))
        sendd = await sython3.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@sython4.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython4.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython4.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@sython4.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await sython4.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@sython4.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython4.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await sython4(JoinChannelRequest('d3boot_7'))
        joinw = await sython4(JoinChannelRequest('Fvvvv'))
        joine = await sython4(JoinChannelRequest('DzDDDD'))
        joinr = await sython4(JoinChannelRequest('botbillion'))
        joint = await sython4(JoinChannelRequest('zzzzzz1'))
        joiny = await sython4(JoinChannelRequest('zzzzzz'))

        joini = await sython4(JoinChannelRequest('zz_MX'))
        joino = await sython4(JoinChannelRequest('zd_e6'))
        joinp = await sython4(JoinChannelRequest('KTTTT'))
        joina = await sython4(JoinChannelRequest('RRXFR'))
        sendd = await sython4.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@sython5.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await sython5.send_message(userbt, '/start')
     sleep(2)
    msg1 = await sython5.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@sython5.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await sython5.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@sython5.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await sython5.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await sython5(JoinChannelRequest('d3boot_7'))
        joinw = await sython5(JoinChannelRequest('Fvvvv'))
        joine = await sython5(JoinChannelRequest('DzDDDD'))
        joinr = await sython5(JoinChannelRequest('botbillion'))
        joint = await sython5(JoinChannelRequest('zzzzzz1'))
        joiny = await sython5(JoinChannelRequest('zzzzzz'))

        joini = await sython5(JoinChannelRequest('zz_MX'))
        joino = await sython5(JoinChannelRequest('zd_e6'))
        joinp = await sython5(JoinChannelRequest('KTTTT'))
        joina = await sython5(JoinChannelRequest('RRXFR'))
        sendd = await sython5.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
        


print("💠 Sython Userbot Running 💠")
sython1.run_until_disconnected()
sython2.run_until_disconnected()
sython3.run_until_disconnected()
sython4.run_until_disconnected()
sython5.run_until_disconnected()

#code skip accumulate points by t.me.zzzzl1l thank you my bro
