#!/usr/bin/env python

from obspy import Stream, Trace, read
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


class Q330_log_reader():

    def __init__(self, file):
        self.file = file
        self.stream = read(file)

    def stdout_read(self):
        self.stream.sort(keys=['starttime'])
        for trace in self.stream:
            print "-------------------------------------------------"
            print  trace.stats.starttime.format_seedlink()
            print ''.join(trace.data).rstrip()

def main():
    parser = ArgumentParser(prog='Q330_log_reader',
                            description='Output human readable logs from Q330 log file ',
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument('logfile', type=file)
    args = parser.parse_args()


    log_reader = Q330_log_reader(args.logfile)
    log_reader.stdout_read()


if __name__ == '__main__':
    main()
