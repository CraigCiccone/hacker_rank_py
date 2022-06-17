# EASY


def timeConversion(s):
    am_pm = s[-2:]
    parts = s[:-2].split(":")
    hour = int(parts[0])

    if hour >= 12 and am_pm == "AM":
        hour -= 12
    elif hour < 12 and am_pm == "PM":
        hour += 12

    return f"{hour:02}:{parts[1]}:{parts[2]}"


if __name__ == "__main__":
    print(timeConversion("12:01:00PM"))
    print(timeConversion("12:01:00AM"))
    print(timeConversion("07:05:45AM"))
    print(timeConversion("07:05:45PM"))
    print(timeConversion("01:05:45PM"))
    print(timeConversion("01:05:45AM"))
    print(timeConversion("12:00:00AM"))
