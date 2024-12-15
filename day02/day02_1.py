def read_reports():
    reports = []
    with open("day02/input.txt", "r") as f:
        for line in f:
            r = [int(num) for num in line.split()]
            reports.append(r)
    return reports

def get_direction(report, i, j):
    delta = report[j] > report[i]
    if delta == 0:
        return 0
    return 1 if delta > 0 else -1

def is_distance_allowed(report, i, j) -> bool:
    d = abs(report[i]-report[j])
    return 1 <= d and d <= 3

def is_safe(report) -> bool:
    if not is_distance_allowed(report, 0, 1):
        return False
    direction = get_direction(report, 0,1)
    #direction = 1 if report[1] > report[0] else -1

    for i in range(2,len(report)):
        if get_direction(report, i-1,i) != direction or not is_distance_allowed(report, i-1,i):
            return False
    return True

def count_safe(reports: list):
    count = 0
    r: list
    for r in reports:
        count += is_safe(r)
    return count

def count_safe_with_tolerate(reports: list):
    count = 0
    r: list
    for r in reports:
        if is_safe(r):
            count += 1
            continue
        for i in range(len(r)):
            new_r = r.copy()
            new_r.pop(i)
            if is_safe(new_r):
                count += 1
                break


    return count

"""
def count_safe_with_tolerate(reports: list):
    count = 0
    r: list
    for r in reports:
        is_safe = True
        can_remove_item = True

        if not is_distance_allowed(r,0,1):
            r = r[1:]
            can_remove_item = False
        elif not is_distance_allowed(r,-2,-1):
            r = r[:-1]
            can_remove_item = False

        prev_direction = get_direction(r,0,1)
        for i in range(1,len(r)):
            if i >= 2 and get_direction(r, i-1, i) != prev_direction:
                if can_remove_item and is_distance_allowed(r,i-2,i):
                    can_remove_item = False
                    prev_direction = get_direction(r,i-2,i)
                    continue
                else:
                    is_safe = False
                    break
            if not is_distance_allowed(r, i-1, i):
                is_safe = False
                break


        count += is_safe
    return count
"""



if __name__ == "__main__":
    reports = read_reports()
    print(f"{count_safe(reports)=}")
    print(f"{count_safe_with_tolerate(reports)=}")
