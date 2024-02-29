#!/usr/bin/env python

import time

import piglow

import schedule


def sleep ():
  piglow.clear()
  piglow.show()
  piglow.orange(75)
  piglow.red(155)
  piglow.show()

def rise ():
  piglow.clear()
  piglow.show()
  piglow.green(75)
  piglow.blue(155)
  piglow.show()

schedule.every().day.at("06:30").do(rise)
schedule.every().day.at("19:00").do(sleep)

while True:
    schedule.run_pending()
    time.sleep(30)
