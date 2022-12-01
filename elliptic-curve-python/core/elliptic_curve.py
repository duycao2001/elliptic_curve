from typing import List
from core.point import POINT_AT_INFINITY, Point
from utils.int_operations import is_prime
from utils.mod_operations import divide, is_square, square_root


class EllipticCurve:
    def __init__(self, a, b, p) -> None:
        # if self.is_non_singular():
        self.__a = a
        self.__b = b
        self.__p = p
        self.__points = self.get_points()

    def is_non_singular(self):
        return 4 * self.__a ** 3 + 27 * self.__b ** 2 != 0

    def get_points(self) -> List[Point]:
        points = []
        for x in range(0, self.__p):
            global y
            x_part = x ** 3 + self.__a * x + self.__b
            if is_square(x_part, self.__p):
                y = square_root(x_part, self.__p)
            else:
                continue

            p1 = Point(x, y)
            if p1.get_y() != 0:
                p2 = Point(x, self.__p - y)
                points.append(p2)
            points.append(p1)

        return points

    def is_on_curve(self, p: Point):
        x, y = p.get_x(), p.get_y()
        return (y ** 2) % self.__p == (x ** 3 + self.__a * x + self.__b) % self.__p

    def add(self, p1: Point, p2: Point):
        if self.is_on_curve(p1) and self.is_on_curve(p2):
            x1, y1 = p1.get_x(), p1.get_y()
            x2, y2 = p2.get_x(), p2.get_y()
            if (p1.equals_to(p2) and y1 == 0) or (not p1.equals_to(p2) and x1 == x2):
                return POINT_AT_INFINITY

            global slope
            if p1.equals_to(p2):
                slope = divide(3 * x1 ** 2 + self.__a, 2 * y1, self.__p)
            else:
                slope = divide(y2 - y1, x2 - x1, self.__p)
            x_sum = (slope ** 2 - x1 - x2) % self.__p
            y_sum = (slope * (x1 - x_sum) - y1) % self.__p

            return Point(x_sum, y_sum)

        if p1.equals_to(POINT_AT_INFINITY) and self.is_on_curve(p2):
            return p2

        if p2.equals_to(POINT_AT_INFINITY) and self.is_on_curve(p1):
            return p1

        return POINT_AT_INFINITY

    def multiply(self, p: Point, k: int):
        point_prod = Point(p.get_x(), p.get_y())
        if self.is_on_curve(p) and k > 0:
            for _ in range(1, k):
                point_prod = point_prod.assign(self.add(point_prod, p))
            return point_prod

        return POINT_AT_INFINITY

    def get_times_table(self, p: Point):
        k = 1
        table = f'P({p.get_x()}, {p.get_y()}):\n'
        while not self.multiply(p, k).equals_to(POINT_AT_INFINITY):
            point_prod = self.multiply(p, k)
            table += f' - {k if k > 1 else ""}P = {point_prod.to_string()}\n'
            k += 1

        table += f' - {k}P = {POINT_AT_INFINITY.to_string()}\n'
        return table

    def get_times_tables(self):
        tables = f'Bảng cửu chương của {self.to_string()}'
        for i, p in enumerate(self.__points):
            k = 1
            table = f'P_{i}({p.get_x()}, {p.get_y()})'
            while not self.multiply(p, k).equals_to(POINT_AT_INFINITY):
                point_prod = self.multiply(p, k)
                table += f' - {k if k > 1 else ""}P_{i} = {point_prod.to_string()}\n'
                k += 1

            table += f' - {k}P_{i} = {POINT_AT_INFINITY.to_string()}\n'
            tables += f'{table}\n'
        return tables

    def to_string(self):
        return f'y^2 = x^3 {"+" if self.__a > 0 else "-"} {abs(self.__a) if abs(self.__a) != 1 else ""}x {"+" if self.__b > 0 else "-"} {abs(self.__b)} (mod {self.__p})'

    def count_points(self):
        return len(self.__points) + 1  # tính cả điểm vô cực

    def is_prime_points_count(self):
        return is_prime(self.count_points())