#!/bin/sh

# Fix style of uncommited po files, or all if --all is given.

if [ z"$1" = z"--all" ]
then
    for po in */*.po
    do
        echo "$po"
        tac "$po" | tac | msgcat - -o "$po"
    done
else
    for po in $(git status | grep 'modified.*\.po$' | rev | cut -d' ' -f1 | rev)
    do
        echo "$po"
        tac "$po" | tac | msgcat - -o "$po"
    done
fi
