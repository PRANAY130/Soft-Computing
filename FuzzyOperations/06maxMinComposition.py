import numpy as np

relAB = np.array([[0.5, 0.7, 0.2],
                  [0.8, 0.6, 0.9]])

relBC = np.array([[0.6, 0.3],
                 [0.9, 0.4],
                 [0.5, 0.8]])

result = []

for i in range (len(relAB)):
    res = []
    for j in range(len(relBC[0])):
        elList = []
        for k in range(len(relBC)):
            el=np.minimum(relAB[i][k], relBC[k][j])
            elList.append(el)
        res.append(max(elList))
    result.append(res)

print(np.array(result))