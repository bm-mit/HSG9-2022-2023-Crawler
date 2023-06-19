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
    __spec_sum_points_by_subject: dict[str, list[float]]

    __math_points: list[float]
    __literature_points: list[float]

    __foreign_points: list[float]
    __foreign_points_by_subject: dict[str, list[float]]
    __foreign_sum_points_by_subject = dict[str, list[float]]

    __spec_points: list[float]
    __spec_points_by_subject: dict[str, list[float]]

    def __init__(self):
        self.csv_rows = []

        self.__contestants = []
        self.__sum_points = []
        self.__spec_sum_points = []

        self.__math_points = []
        self.__literature_points = []
        self.__foreign_points = []
        self.__spec_points = []

        self.__spec_sum_points_by_subject = {}
        self.__foreign_points_by_subject = {}
        self.__spec_points_by_subject = {}
        self.__foreign_sum_points_by_subject = {}

    def add_contestant(self, contestant: Contestant) -> None:
        """"""
        self.__contestants.append(contestant)

        points = contestant.points
        normal_point = points.math + points.literature + points.foreign
        self.__math_points.append(points.math)
        self.__literature_points.append(points.literature)
        self.__foreign_points.append(points.foreign)
        self.__sum_points.append(normal_point)
        
        self.csv_rows.append(
            [contestant.id_code, contestant.full_name, points.math, points.literature, points.foreign, points.foreign_lang, points.spec, points.isspec, points.spec_subject]
        )

        try:
            self.__foreign_points_by_subject[points.foreign_lang].append(
                points.foreign_lang)
        except Exception:
            self.__foreign_points_by_subject[points.foreign_lang] = [
                points.foreign]

        if points.isspec:
            self.__spec_points.append(points.spec)
            self.__spec_sum_points.append(normal_point + points.spec * 2)

            try:
                self.__spec_points_by_subject[points.spec_subject].append(
                    points.spec)
            except Exception:
                self.__spec_points_by_subject[points.spec_subject] = [
                    points.foreign]

            try:
                self.__spec_sum_points_by_subject[points.foreign_lang].append(
                    normal_point + points.spec * 2)
            except Exception:
                self.__spec_sum_points_by_subject[points.foreign_lang] = [
                    normal_point + points.spec * 2]

            try:
                self.__foreign_sum_points_by_subject[points.foreign_lang].append(
                    normal_point + points.foreign_lang)
            except Exception:
                self.__foreign_sum_points_by_subject[points.foreign_lang] = [
                    normal_point + points.foreign]

    def save_data(self):
        data = open("statics.txt", "w+", encoding="utf-8")
        csvwrite = csv.writer(data)
        csvwrite.writerows(self.csv_rows)

    def generate(self):
        plt.hist(self.__sum_points)
        plt.title("Sum normal points")
        plt.savefig("SumNormalPoint.png")

        plt.hist(self.__spec_sum_points)
        plt.title("Specialized sum points")
        plt.savefig("SpecSumPoint.png")

        plt.hist(self.__math_points)
        plt.title("Math points")
        plt.savefig("MathPoints.png")

        plt.hist(self.__literature_points)
        plt.title("Literature Points")
        plt.savefig("LiteraturePoints.png")

        plt.hist(self.__foreign_points)
        plt.title("Foreign Points")
        plt.savefig("ForeignPoints.png")

        plt.hist(self.__spec_points)
        plt.title("Specialized Points")
        plt.savefig("SpecPoints.png")

        # plt.hist(self.__spec_sum_points_by_subject, lable="")
        # plt.savefig("aa.png")
        # plt.hist(self.__foreign_points_by_subject, lable="")
        # plt.savefig("aa.png")
        # plt.hist(self.__spec_points_by_subject, lable="")
        # plt.savefig("aa.png")
        # plt.hist(self.__foreign_sum_points_by_subject, lable="")
        # plt.savefig("aa.png")


if __name__ == "__main__":
    p = PlotGenerator()
    p.add_contestant(Contestant("0123", "Bình Minh (test unicode: á ơ ộ à ợ)", Points(
        0.1, 0.2, 0.3, "eng", 0.3, True, "french")))
    p.generate()
    p.save_data()
