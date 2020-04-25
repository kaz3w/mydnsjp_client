#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import argparse
import requests

# Your MyDNS.JP MasterID, Password
MYDNSJP_MID = "id"
MYDNSJP_PWD = "passwd"

# IP Detect service
IP_DETECT_SERVICE = "http://ip1.dynupdate.no-ip.com/"

parser = argparse.ArgumentParser(description="MyDNS.JP client")
parser.add_argument("-r", "--reset", help="Reset address to 0.0.0.0", action="store_true")
parser.add_argument("-v", "--verbose", help="Verbosity", action="store_true")
parser.add_argument("-d", "--dryrun", help="Dry-run (for checking)", action="store_true")
args = parser.parse_args()

if args.reset:
    extip = "0.0.0.0"
else:
    extip = requests.get( IP_DETECT_SERVICE ).text

if args.verbose:
    print( "extip: " + extip )

dns_url = "https://www.mydns.jp/directip.html?MID=" + MYDNSJP_MID + "&PWD=" + MYDNSJP_PWD + "&IPV4ADDR=" + extip

if args.dryrun:
    print( "[dryrun] " + dns_url )
else:
    dnsr = requests.get( dns_url )
    if args.verbose:
        print( dns_url )
        print( "result: " + str(dnsr.status_code) )

