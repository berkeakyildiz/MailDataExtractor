#
# Created by Berke Akyıldız on 10/July/2019
#
# coding: utf-16
import mailbox
import re

filePath = "C:\\Users\\MONSTER\\Desktop\\Starred.mbox"


def prettify(mstring):
    mstring = mstring.replace("=", "")
    mstring = mstring.replace("\n", "")
    mstring = mstring.replace("C3B6", "Ö")
    mstring = mstring.replace("&Ouml;", "Ö")
    mstring = mstring.replace("C3BC", "Ü")
    mstring = mstring.replace("&Uuml;", "Ü")
    mstring = mstring.replace("&uuml;", "ü")
    mstring = mstring.replace("C49E", "Ğ")
    mstring = mstring.replace("C49F", "ğ")
    mstring = mstring.replace("&ouml;", "ö")
    mstring = mstring.replace("&ccedil;", "ç")
    mstring = mstring.replace("C4B1", "ı")
    mstring = mstring.replace("&reg;", "®")
    mstring = mstring.replace("C4B0", "İ")
    mstring = mstring.replace("C59F", "ş")
    mstring = mstring.replace("3D", "=")
    mstring = mstring.replace("09", "\t")
    mstring = mstring.replace("C59E", "Ş")
    mstring = mstring.replace("&#39;", "\'")
    mstring = mstring.replace("&nbsp;", " ")
    return mstring


for message in mailbox.mbox(filePath):
    mstring = message.as_string()
pretty_string = prettify(mstring)
print(pretty_string)

index_labels = pretty_string.find("Labels: ")
index_delivered_to = pretty_string.find("Delivered-To: ")
index_received = pretty_string.find("Received: ")
index_google_smtp_source = pretty_string.find("X-Google-Smtp-Source: ")

labels = pretty_string[index_labels+8:index_delivered_to].split(",")
delivered_to = pretty_string[index_delivered_to+14:index_received]
received = pretty_string[index_received+10:index_google_smtp_source]
rex = r"^(?:\s*(Sun|Mon|Tue|Wed|Thu|Fri|Sat),\s*)?(0?[1-9]|[1-2][0-9]|3[01])\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(19[0-9]{2}|[2-9][0-9]{3}|[0-9]{2})\s+(2[0-3]|[0-1][0-9]):([0-5][0-9])(?::(60|[0-5][0-9]))?\s+([-\+][0-9]{2}[0-5][0-9]|(?:UT|GMT|(?:E|C|M|P)(?:ST|DT)|[A-IK-Z]))(\s*\((\\\(|\\\)|(?<=[^\\])\((?<C>)|(?<=[^\\])\)(?<-C>)|[^\(\)]*)*(?(C)(?!))\))*\s*$"

print("labels: ", labels)
