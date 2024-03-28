#!/usr/bin/python3
import sys
total_size = count = 0
# 200, 301, 400, 401, 403, 404, 405 and 500
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}


def print_stats():
    print("File size: {}".format(total_size))
    for key, val in codes.items():
        if val:
            print("{}: {}".format(key, val))


try:
    for line in sys.stdin:
        values = line.split(" ")
        if len(values) > 2:
            code = values[-2]
            size = int(values[-1])
            if code in codes:
                codes[code] += 1
            total_size += size
            count += 1
            if count == 10:
                count = 0
                print_stats()
finally:
    print_stats()
