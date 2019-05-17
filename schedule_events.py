#!/usr/bin/env python

# Calendar
# Problem
#
# Implement a Calendar class which supports two operations:
#
# Schedule events
# Find time windows which are overbooked and find the associated conflicted events.
# Instructions
#
# Please implement schedule and find_conflicted_time_windows. The return value of find_conflicted_time_windows should be a list of ConflictedTimeWindow objects ordered by their start_time from earliest to latest. Please be aware that each ConflictedTimeWindow should contain ALL the conflicted events within the associated time period.
#
# For example,
#
# calendar = Calendar()
# calendar.schedule(Event(4,
#      datetime.strptime('2014-01-02 10:00', '%Y-%m-%d %H:%M'),
#      datetime.strptime('2014-01-02 11:00', '%Y-%m-%d %H:%M')))
# calendar.schedule(Event(5,
#      datetime.strptime('2014-01-02 09:30', '%Y-%m-%d %H:%M'),
#      datetime.strptime('2014-01-02 11:30', '%Y-%m-%d %H:%M')))
# calendar.schedule(Event(6,
#      datetime.strptime('2014-01-02 08:30', '%Y-%m-%d %H:%M'),
#      datetime.strptime('2014-01-02 12:30', '%Y-%m-%d %H:%M')))
#
# print calendar.find_conflicted_time_windows()
# # Should print something like the following
# # [ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 9, 30),
# #                       end_time=datetime.datetime(2014, 1, 2, 10, 0),
# #                       conflicted_event_ids=[5, 6]),
# # ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 10, 0),
# #                      end_time=datetime.datetime(2014, 1, 2, 11, 0),
# #                      conflicted_event_ids=[4, 5, 6]),
# # ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 11, 0),
# #                      end_time=datetime.datetime(2014, 1, 2, 11, 30),
# #                      conflicted_event_ids=[5, 6])]
#



from datetime import datetime
from collections import namedtuple

import sys

Event = namedtuple('Event', ['id', 'start_time', 'end_time'])
ConflictedTimeWindow = namedtuple('ConflictedTimeWindow', ['start_time', 'end_time', 'conflicted_event_ids'])

class Calendar(object):
    # Should allow multiple events to be scheduled over the same time window.

    def __init__(self):
        self.events = []
        self.conflicts = []

    def schedule(self, event):
        self.events.append(event)

        # # Find out conflict first to save from complexity
        # if len(self.events) > 1:
        #     for e in self.events:
        #
        #         if event.start_time < e.start_time and event.end_time > e.start_time:
        #             conflict_event = ConflictedTimeWindow(event.start_time, event.end_time, [event.id, e.id])
        #             self.conflicts.append(conflict_event)
        #             continue
        #         if e.start_time < event.start_time and e.end_time > event.start_time:
        #             conflict_event = ConflictedTimeWindow(event.start_time, event.end_time, [event.id, e.id])
        #             self.conflicts.append(conflict_event)
        #             continue

    def find_conflicted_time_windows(self):
        # IMPLEMENT ME
        if len(self.events) > 1:
            # selection-sort-like compare
            for i in range(len(self.events) - 1):
                for j in range(i, len(self.events)):
                    e1, e2 = self.events[i], self.events[j]

                    if e1.start_time < e2.start_time and e1.end_time > e2.start_time:
                        conflict_event = ConflictedTimeWindow(e2.start_time, e1.end_time, [e1.id, e2.id])
                        self.conflicts.append(conflict_event)
                        continue
                    if e2.start_time < e1.start_time and e2.end_time > e1.start_time:
                        conflict_event = ConflictedTimeWindow(e1.start_time, e2.end_time, [e1.id, e2.id])
                        self.conflicts.append(conflict_event)
                        continue

        # TODO: Optimize conflicts (down to 15-min interval)

        return self.conflicts


def main(argv):
    calendar = Calendar()
    calendar.schedule(Event(1,
        datetime.strptime('2014-01-01 10:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-01 11:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(2,
        datetime.strptime('2014-01-01 11:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-01 12:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(3,
        datetime.strptime('2014-01-01 12:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-01 13:00', '%Y-%m-%d %H:%M')))

    calendar.schedule(Event(4,
        datetime.strptime('2014-01-02 10:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-02 11:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(5,
        datetime.strptime('2014-01-02 09:30', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-02 11:30', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(6,
        datetime.strptime('2014-01-02 08:30', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-02 12:30', '%Y-%m-%d %H:%M')))

    calendar.schedule(Event(7,
        datetime.strptime('2014-01-03 10:00', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-03 11:00', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(8,
        datetime.strptime('2014-01-03 09:30', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-03 10:30', '%Y-%m-%d %H:%M')))
    calendar.schedule(Event(9,
        datetime.strptime('2014-01-03 09:45', '%Y-%m-%d %H:%M'),
        datetime.strptime('2014-01-03 10:45', '%Y-%m-%d %H:%M')))

    # print(calendar.find_conflicted_time_windows())
    for i in calendar.find_conflicted_time_windows():
        print(i)

    # Should print something like the following

    # [ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 9, 30),
    #                       end_time=datetime.datetime(2014, 1, 2, 10, 0),
    #                       conflicted_event_ids=[5, 6]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 10, 0),
    #                       end_time=datetime.datetime(2014, 1, 2, 11, 0),
    #                       conflicted_event_ids=[4, 5, 6]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 2, 11, 0),
    #                       end_time=datetime.datetime(2014, 1, 2, 11, 30),
    #                       conflicted_event_ids=[5, 6]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 3, 9, 45),
    #                       end_time=datetime.datetime(2014, 1, 3, 10, 0),
    #                       conflicted_event_ids=[8, 9]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 3, 10, 0),
    #                       end_time=datetime.datetime(2014, 1, 3, 10, 30),
    #                       conflicted_event_ids=[7, 8, 9]),
    #  ConflictedTimeWindow(start_time=datetime.datetime(2014, 1, 3, 10, 30),
    #                       end_time=datetime.datetime(2014, 1, 3, 10, 45),
    #                       conflicted_event_ids=[7, 9])]

main("")
