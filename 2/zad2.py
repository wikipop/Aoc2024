import math

def check_report(levels):
    last_diff = 0
    for i in range(1, len(levels)):
        diff = int(levels[i]) - int(levels[i - 1])

        if last_diff != 0 and math.copysign(1, diff) != math.copysign(1, last_diff):
            return False

        if abs(diff) > 3 or abs(diff) < 1:
            return False

        last_diff = diff
    else:
        return True

with open("input.txt") as f:
    S = sum(
        check_report(report.split()) or any(
            check_report(report.split()[:i] + report.split()[i+1:]) for i in range(len(report))
        )
        for report in f
    )

print(S)