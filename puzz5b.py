import re


class Line(object):
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        x_min = min(x0, x1)
        x_max = max(x0, x1)
        y_min = min(y0, y1)
        y_max = max(y0, y1)

        # if horizontal or vertical line
        if (x_min == x_max) or (y_min == y_max):
            self.line = set(
                (x, y)
                for x in range(x_min, x_max+1)
                for y in range(y_min, y_max+1)
            )
        # if 45-degree diagonal line
        else:
            steps = (x_max - x_min)
            line = []
            for step in range(steps+1):
                is_y_declining = ((x1 - x0) < 0)
                is_x_declining = ((y1 - y0) < 0)
                if is_y_declining:
                    y = y_max - step
                else:
                    y = y_min + step
                if is_x_declining:
                    x = x_max - step
                else:
                    x = x_min + step
                line.append((x, y))
            self.line = set(line)

    def __repr__(self):
        return f'Line(x0={self.x0}, x1={self.x1}, y0={self.y0}, y1={self.y1})'

    def intersect(self, line):
        return self.line.intersection(line)


# helpers
def clean_line(line_txt):
    return Line(
        *list(map(int, re.findall(r'(\d{1,6})', line_txt)))
    )


def read_input():
    with open('inputs/input5.txt') as fh:
        clean_lines = list(
            map(clean_line, fh.readlines())
        )
    return clean_lines 


# main
def filter_lines(l):
    if ((l.x0 == l.x1) or (l.y0 == l.y1)):
        return l


def find_overlap():
    all_lines = read_input()
    # lines = list(filter(filter_lines, all_lines))
    lines = all_lines
    intersections = set()

    for line0 in lines:
        # need to compare each line with each other line
        for line1 in lines:
            if line0 == line1:
                continue
            maybe_intersection = line0.intersect(line1.line)
            if maybe_intersection:
                intersections.update(maybe_intersection)
    return len(intersections)


_runner = find_overlap
