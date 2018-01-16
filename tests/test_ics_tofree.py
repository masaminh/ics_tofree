from unittest import TestCase
import ics_tofree.ics_tofree as tofree
from icalendar import Calendar


class TestIcsToFree(TestCase):
    def test_update_transp_opaque_transparent(self):
        ical = '''BEGIN:VCALENDAR
PRODID:-//A//B//EN
VERSION:2.0
BEGIN:VEVENT
DTSTART;VALUE=DATE:20180422
DTEND;VALUE=DATE:20180423
DTSTAMP:20171027T031747Z
CREATED:19000101T120000Z
DESCRIPTION:
LAST-MODIFIED:20171027T031657Z
SUMMARY:summary
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR'''

        cal = Calendar.from_ical(ical)
        tofree.update_transp(cal, 'TRANSPARENT')
        ev = [c for c in cal.walk() if c.name == 'VEVENT'][0]
        self.assertEqual(ev['TRANSP'], 'TRANSPARENT')

    def test_update_transp_none_transparent(self):
        ical = '''BEGIN:VCALENDAR
PRODID:-//A//B//EN
VERSION:2.0
BEGIN:VEVENT
DTSTART;VALUE=DATE:20180422
DTEND;VALUE=DATE:20180423
DTSTAMP:20171027T031747Z
CREATED:19000101T120000Z
DESCRIPTION:
LAST-MODIFIED:20171027T031657Z
SUMMARY:summary
END:VEVENT
END:VCALENDAR'''

        cal = Calendar.from_ical(ical)
        tofree.update_transp(cal, 'TRANSPARENT')
        ev = [c for c in cal.walk() if c.name == 'VEVENT'][0]
        self.assertEqual(ev['TRANSP'], 'TRANSPARENT')

    def test_update_transp_transparent_opaque(self):
        ical = '''BEGIN:VCALENDAR
PRODID:-//A//B//EN
VERSION:2.0
BEGIN:VEVENT
DTSTART;VALUE=DATE:20180422
DTEND;VALUE=DATE:20180423
DTSTAMP:20171027T031747Z
CREATED:19000101T120000Z
DESCRIPTION:
LAST-MODIFIED:20171027T031657Z
SUMMARY:summary
TRANSP:TRANSPARENT
END:VEVENT
END:VCALENDAR'''

        cal = Calendar.from_ical(ical)
        tofree.update_transp(cal, 'OPAQUE')
        ev = [c for c in cal.walk() if c.name == 'VEVENT'][0]
        self.assertEqual(ev['TRANSP'], 'OPAQUE')
