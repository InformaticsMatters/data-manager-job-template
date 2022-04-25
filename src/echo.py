#!/usr/bin/env python
"""Template echo utility.
"""
import argparse
import os

# Import Data Manager DmLog utility.
# Messages emitted using this result in Task Events.
from dm_job_utilities.dm_log import DmLog


def run(msg: str, output_filename: str) -> None:
    """Prints the supplied message.
    """
    DmLog.emit_event(f"msg: {msg}")

    with open(output_filename, 'wt') as output:
        output.write(msg)
    os.chmod(output_filename, 0o664)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Job Template Jobs")
    parser.add_argument("-m", "--msg", required=True, help="A message to print")
    parser.add_argument("-o", "--out", required=True, help="The output file")
    args = parser.parse_args()

    run(args.msg, args.out)
