from percomplex import PerComplex
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def main():
    percomplex = PerComplex(1, 1, 2)
    percomplex2 = PerComplex(2, 3, 6)
    print(percomplex)
    print(percomplex * percomplex)
    # print(percomplex2)
    mult_per = percomplex * percomplex2
    # print(mult_per)
    # print(mult_per / 2)
    print(percomplex ** 2)
    unreal = PerComplex(0, 1, 1)
    print(unreal ** 4)


    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    #
    # # For each set of style and range settings, plot n random points in the box
    # # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    # new_percomplex = percomplex
    # for percomplex_num in percomplex.get_next_members(10):
    #     # ax.scatter(*percomplex_num.coordinates)
    #     new_percomplex *= percomplex_num
    #     ax.scatter(*new_percomplex.coordinates)
    #     # ax.scatter(*(percomplex*percomplex_num).coordinates)
    #
    # ax.set_xlabel('Real')
    # ax.set_ylabel('Imaginary')
    # ax.set_zlabel('Perplex')
    # plt.show()


if __name__ == '__main__':
    main()

