import argparse
from icalendar import Calendar
import sys


def update_transp(cal, transp):
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            ev['TRANSP'] = 'TRANSPARENT'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?',
                        type=argparse.FileType(mode='r'), default=sys.stdin)
    parser.add_argument('-o', '--output', nargs='?',
                        type=argparse.FileType(mode='w'), default=sys.stdout)
    args = parser.parse_args()

    cal = Calendar.from_ical(args.input.read())
    update_transp(cal, 'TRANSPARENT')

    args.output.write(cal.to_ical().decode('utf-8'))


if __name__ == '__main__':
    main()
