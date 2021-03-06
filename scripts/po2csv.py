#!/usr/bin/env python3

import csv
import polib


def po2csv(csvfile, pofile, untranslated_only=False):
    po = polib.pofile(pofile)
    with open(csvfile, 'w', newline='') as opened_csvfile:
        csvwriter = csv.writer(opened_csvfile)
        for entry in po:
            if untranslated_only == False or entry.msgstr == '':
                csvwriter.writerow([entry.msgid, entry.msgstr])


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description="Create a CSV file from a PO file.")
    parser.add_argument('pofile')
    parser.add_argument('csvfile')
    parser.add_argument('--untranslated-only', action='store_true')
    return parser.parse_args()

if __name__ == '__main__':
    po2csv(**vars(parse_args()))
