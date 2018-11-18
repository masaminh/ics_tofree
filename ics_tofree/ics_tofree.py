"""Calendarファイル(.ics)内のイベントをすべて「予定なし」に書き換える."""
import argparse
from icalendar import Calendar
import sys


def update_transp(cal, transp):
    """VEVENTコンポーネントのTRANSPプロパティを指定のものに書き換える."""
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            ev['TRANSP'] = transp


def main():
    """メイン関数."""
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
