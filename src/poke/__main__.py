
"""
Made by PurpleLemons-dev for CyberThing with Python v3.11.1
"""

import argparse
from datetime import datetime as dt

parser = argparse.ArgumentParser(description="Network recon by Poke.")
parser.add_argument("-d", "--debug", action="store_true", help="Enables debug mode.")
parser.add_argument("--log","--format", metavar="'<fmt>'", type=str, help="The format for the log message. !ip is the client IP, !date is the day in YYYY/MM/DD, !time is the time in HH:MM:SS, !method is the HTTP request method, !path is the URI, !status is the HTTP response code, and !proto is the HTTP protocol version the request is made over.")
parser.add_argument("-s", "--save", action="store_true", help="Saves the log to a file.")
parser.add_argument("scan", type=str, help="Will scan the current interface. Use CDIR notation, e.g. 192.168.0.0/24")

args = parser.parse_args()


