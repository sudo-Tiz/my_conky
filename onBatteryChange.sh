#!/bin/bash

nohup bash ~/.config/conky/launchConky.sh </dev/null >/dev/null 2>&1 &
on_ac_power
PREVIOUS=$(echo $?)

while [ 1 ]; do
    # check if we're on ac power or not
    on_ac_power
    CURRENT=$(echo $?)
    if [ $CURRENT -ne $PREVIOUS ]; then
        if [ $CURRENT -eq 0 ]; then
            nohup bash ~/.config/conky/launchConky.sh </dev/null >/dev/null 2>&1 &
        else
            killall conky
        fi
        PREVIOUS=$(echo $CURRENT )
    fi
    sleep 10
done
