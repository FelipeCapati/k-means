from kmeans import Kmeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("./data/bianchi.csv")

kmeans = Kmeans()
kmeans.fit(k=3,
           data=data,
           centroid_centers=np.array([[1., 1.], [3., 3.], [5., 5.]])
           )

plt.scatter(data['x'].iloc[np.where(kmeans.classes == 0)[0]].values,
            data['y'].iloc[np.where(kmeans.classes == 0)[0]].values,
            c='blue',
            label='data class 0')
plt.scatter(data['x'].iloc[np.where(kmeans.classes == 1)[0]].values,
            data['y'].iloc[np.where(kmeans.classes == 1)[0]].values,
            c='green',
            label='data class 1')
plt.scatter(data['x'].iloc[np.where(kmeans.classes == 2)[0]].values,
            data['y'].iloc[np.where(kmeans.classes == 2)[0]].values,
            c='red',
            label='data class 2')
plt.scatter(kmeans.centroid_centers[:, 0], kmeans.centroid_centers[:, 1], c='yellow', label='centroid_center')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()