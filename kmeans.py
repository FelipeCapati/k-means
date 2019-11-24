import numpy as np
import pandas as pd
from random import uniform


class Kmeans:
    def __init__(self):
        self.data = None
        self.centroid_centers = None
        self.classes = None

    @staticmethod
    def __euclidian_distance(p1: np.ndarray, p2: np.ndarray) -> float:
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def __get_random_centroid_centers(self, k: int) -> np.array:
        describe = self.data.describe()

        # Define space to create a random centroid center
        lim_x_min = describe['x'].min()
        lim_x_max = describe['x'].max()
        lim_y_min = describe['y'].min()
        lim_y_max = describe['y'].max()

        centroid_centers = np.zeros([k, 2])
        for i in range(k):
            centroid_centers[i, 0] = uniform(lim_x_min, lim_x_max)
            centroid_centers[i, 1] = uniform(lim_y_min, lim_y_max)

        return centroid_centers

    def __get_data_classes(self, k:int, centroid_centers: np.array) -> np.array:
        data_length = len(self.data)
        np_classes = np.zeros([data_length])
        for i in range(data_length):
            point = self.data.iloc[i].values
            centers_distance = np.zeros([k])
            for j in range(k):
                centers_distance[j] = self.__euclidian_distance(p1=centroid_centers[j], p2=point)
            np_classes[i] = np.where(centers_distance == np.amin(centers_distance))[0][0]
        return np_classes

    def __update_centroid_centers(self, centroid_centers: np.array, np_classes: np.array):
        for update_class in np.unique(np_classes).astype(int):
            centroid_centers[update_class][0] = self.data.iloc[np.where(np_classes == update_class)[0]].describe()['x']['mean']
            centroid_centers[update_class][1] = self.data.iloc[np.where(np_classes == update_class)[0]].describe()['y']['mean']
        return centroid_centers

    def fit(self, k: int, data: pd.DataFrame, centroid_centers: np.array, random: bool = False, n: int = 100):
        self.data = data
        if random:
            centroid_centers = self.__get_random_centroid_centers(k=k)
        count = 0
        while count < n:
            self.classes = self.__get_data_classes(k=k, centroid_centers=centroid_centers)
            centroid_centers = self.__update_centroid_centers(centroid_centers=centroid_centers, np_classes=self.classes)
            count += 1

        self.centroid_centers = centroid_centers
