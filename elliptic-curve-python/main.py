from random import randrange
from time import time
from core.elliptic_curve import EllipticCurve
from core.point import POINT_AT_INFINITY

from utils.constants import PRIME_NUMBERS_2_TO_4_DIGITS



a, b = 1, 6

# các giá trị p sao cho tổng số điểm trên đường cong elliptic là số nguyên tó
prime_elliptic_curve = []
# c = list(filter(lambda x: 10 <= x <= 99, PRIME_NUMBERS_2_TO_4_DIGITS))

# tìm p có 2 chữ số để tổng số điểm trên đường cong elliptic là số nguyên tố
start_time = time()
for p in PRIME_NUMBERS_2_TO_4_DIGITS:
    curve = EllipticCurve(a, b, p)
    if curve.is_prime_points_count():
        prime_elliptic_curve.append(p)
        print(f'p = {p}, số điểm = {curve.count_points()}')
print(f'thời gian tìm p: {time() - start_time}')

# bảng cửu chương của các điểm thuộc đường cong elliptic
# với p được chọn ngẫu nhiên trong mảng prime_elliptic_curve
rand_index = randrange(0, len(prime_elliptic_curve))
rand_p = prime_elliptic_curve[rand_index]
rand_curve = EllipticCurve(a, b, rand_p)
print(f'bảng cửu chương với p = {rand_p}')
global point
while True:
    point_index = randrange(0, rand_curve.count_points())
    point = rand_curve.get_points()[point_index]
    if not point.equals_to(POINT_AT_INFINITY):
        break
start_time = time()
print(rand_curve.get_times_table(point))
print(f'thời gian liệt kê bảng cửu chương: {time() - start_time}')