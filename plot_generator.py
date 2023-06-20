"""
Provides generating plots features.
"""

import csv
from prettytable import PrettyTable
from contestant import Contestant
from points import Points
from matplotlib import pyplot as plt


class PlotGenerator:
    """"""

    __contestants: list[Contestant]

    __sum_points: list[float]
    __spec_sum_points: list[float]

    __math_points: list[float]
    __literature_points: list[float]
    __foreign_points: list[float]
    __spec_points: list[float]

    def __init__(self):
        self.csv_rows = []

        self.__contestants = []
        self.__sum_points = []
        self.__spec_sum_points = []

        self.__math_points = []
        self.__literature_points = []
        self.__foreign_points = []
        self.__spec_points = []
        
        data = open("statics.csv", "w+", encoding="utf-8")
        self.csvwriter = csv.writer(data)
        self.csvwriter.writerow(("ID", "FULL_NAME", "MATH", "LITERATURE", "FOREIGN", "SPEC", "IS_SPEC"))

    def add_contestant(self, contestant: Contestant) -> None:
        """"""
        self.__contestants.append(contestant)

        points = contestant.points
        normal_point = points.math + points.literature + points.foreign
        self.__math_points.append(points.math)
        self.__literature_points.append(points.literature)
        self.__foreign_points.append(points.foreign)
        self.__sum_points.append(normal_point)
        
        self.csvwriter.writerow(
            [contestant.id_code, contestant.full_name, points.math, points.literature, points.foreign, points.spec, points.isspec]
        )

        if points.isspec:
            self.__spec_points.append(points.spec)
            self.__spec_sum_points.append(normal_point + points.spec * 2)

    def generate(self):
        plt.hist(self.__sum_points)
        plt.title("Sum normal points")
        plt.savefig("SumNormalPoint.png")
        plt.clf()

        plt.hist(self.__spec_sum_points)
        plt.title("Specialized sum points")
        plt.savefig("SpecSumPoint.png")
        plt.clf()

        plt.hist(self.__math_points)
        plt.title("Math points")
        plt.savefig("MathPoints.png")
        plt.clf()

        plt.hist(self.__literature_points)
        plt.title("Literature Points")
        plt.savefig("LiteraturePoints.png")
        plt.clf()

        plt.hist(self.__foreign_points)
        plt.title("Foreign Points")
        plt.savefig("ForeignPoints.png")
        plt.clf()

        plt.hist(self.__spec_points)
        plt.title("Specialized Points")
        plt.savefig("SpecPoints.png")
        plt.clf()


if __name__ == "__main__":
    p = PlotGenerator()
    p.add_contestant(Contestant("0123", "Bình Minh (test unicode: á ơ ộ à ợ ế)", Points(
        0.1, 0.2, 0.5, "eng", 0.3, True, "french")))
    p.add_contestant(Contestant("0123", "Bình Minh (test unicode: á ơ ộ à ợ ế)", Points(
        0.1, 0.2, 0.8, "eng", 0.2, True, "french")))
    p.generate()
    p.save_data()
