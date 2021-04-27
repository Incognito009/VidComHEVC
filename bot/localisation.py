#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "👋🏻 <b>Hi Bruh!</b> \n\nI'm <b>High Efficiency Video Compressor 🗳</b> \n\nSend or Foward Me Any Telegram Big Video File I'll Compress It To A Small Video File For You! \n\n<i>Please Hit /help For More Details...😌</i>"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading ... \n"
    
    UPLOAD_START = "📤 Uploading ... \n"
    
    COMPRESS_START = "📀 Trying to Compress ... "
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} Seconds.\nDetected File Size: {}\nSorry. But, I Cannot Upload Files Greater Than 1.95GB Due To Telegram API Limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\n© @AsmSafone | @SafoTheBot"

    COMPRESS_PROGRESS = "⏳ Time Left: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "Already A Process Going On! ⚠️ \n\nPlease Come Back After A While.\nCheck Live Status on Status Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "High Efficiency Video Compressor Bot 🗳\n<i>Send Me Your Telegram Big Video File In Video or File Format & I Will Compress That To Small Video Without Lossing Video Quality.</i>\n\nNote: Sometimes Little Quality May Decrease If Video Is Of Low Quality. I Consume 3 Times More Time Than Other Compressors Do This Process! 🤒"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
