#!/usr/bin/env python
# encoding: utf-8
import datetime
import sys


def print_colored(s):
    RED_CL_START = '\033[91m'
    CL_END = '\033[0m'
    sys.stdout.write(RED_CL_START + s + CL_END)


def progress(width, percent):
    sys.stdout.write('[')
    step = 100 / width
    tmp = percent
    while tmp > 0:
        sys.stdout.write('=')
        tmp -= step
        width -= 1
    while width > 0:
        sys.stdout.write(' ')
        width -= 1
    sys.stdout.write('] %d%%\n' % percent)


def main():
    today = datetime.date.today()
    birth_year = birth_month = 0

    while not (birth_year >= 1900 and birth_year <= today.year
            and birth_month >= 1 and birth_month <= 12):
        birth = raw_input("Enter your birthday(yyyy.mm):").split('.')
        birth = map(int, birth)
        birth_year = birth[0]
        birth_month = birth[1]

    passed_months = (today.year - birth_year) * 12 + today.month - birth_month
    total = 900
    if passed_months < 0:
        print "Hi, can I use your time machine? future guy."
        return

    print "Passed months: %d. The rest of your life: %d months" \
        % (passed_months, total - passed_months)
    progress(50, passed_months * 100 / total)

    while total > 0:
        total -= 1
        sys.stdout.write('|')
        if passed_months > 0:
            print_colored('x')
            passed_months -= 1
        else:
            sys.stdout.write(' ')
        if total % 30 == 0:
            sys.stdout.write('|\n')


if __name__ == '__main__':
    main()
