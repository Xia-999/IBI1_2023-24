import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
condition = arr_2d > 2
indices = np.where(condition)
print("满足条件的元素的索引：", indices)
print("满足条件的元素：", arr_2d[condition])