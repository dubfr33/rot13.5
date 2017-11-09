#!/usr/bin/env python
import argparse

def rot_encode(clr_str):

    rot_chars = []

    for ch in clr_str:
        ch_dec = ord(ch)
        if 65 <= ch_dec <= 90:
            rot_chars.append(chr((ch_dec + 13) % 65 % 26 + 65))
        elif 97 <= ch_dec <= 122:
            rot_chars.append(chr((ch_dec + 13) % 97 % 26 + 97))
        elif 48 <= ch_dec <= 57:
            rot_chars.append(chr((ch_dec + 5) % 48 % 10 + 48))
        else:
            rot_chars.append(ch)

    return ''.join(rot_chars)

def rot_decode(enc_str):

    rot_chars = []

    for ch in enc_str:
        ch_dec = ord(ch)
        if 65 <= ch_dec <= 90:
            rot_chars.append(chr((ch_dec % 65 - 13) % 26 + 65))
        elif 97 <= ch_dec <= 122:
            rot_chars.append(chr((ch_dec % 97 - 13) % 26 + 97))
        elif 48 <= ch_dec <= 57:
            rot_chars.append(chr((ch_dec % 48 - 5) % 10 + 48))
        else:
            rot_chars.append(ch)

    return ''.join(rot_chars)

parser = argparse.ArgumentParser(
	epilog='Example: rot.py [-e,-d] somestring')
parser.add_argument("-e", help="String to encode")
parser.add_argument("-d", help="String to decode")
args = parser.parse_args()
if args.e:
	enc_str = rot_encode(args.e)
	print "Encoded string: '%s'" % enc_str
elif args.d:
	dec_str = rot_decode(args.d)
	print "Decoded string: '%s'" % dec_str
else:
	parser.print_help()
