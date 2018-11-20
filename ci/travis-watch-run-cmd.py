#!/usr/bin/env python3

import os
import time
import click


@click.command()
def main():
    """Watch last travis-ci run docker cmd from log"""
    MAX_TIMEOUT = 30 * 60  # Maximum to wait 30 minutes
    POLL_INTERVAL = 60

    old_size = os.stat('cmd-run.log').st_size
    for elapsed in range(0, MAX_TIMEOUT//POLL_INTERVAL):

        time.sleep(POLL_INTERVAL)

        new_size = os.stat('cmd-run.log').st_size
        if new_size == old_size:
            print("No more output in last minute!")
            break

        print("Checking ...")

    return 0


if __name__ == '__main__':
    main()
