#!/bin/sh
find . -name \*.po -execdir msgfmt chatterbot.po -o chatterbot.mo \;
