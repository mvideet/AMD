array = [0.75, 0.6842105263157896, 0.7567567567567567, 0.6875, 0.6428571428571429, 0.7500000000000001,
         0.6857142857142857, 0.5555555555555556, 0.6875, 0.6206896551724138, 0.4827586206896552, 0.625,
         0.5517241379310345, 0.6153846153846154, 0.7894736842105263, 0.6818181818181818, 0.5806451612903225,
         0.6341463414634146, 0.7368421052631577, 0.5909090909090909, 0.7272727272727272, 0.6285714285714287,
         0.7727272727272727, 0.6470588235294117, 0.5294117647058824, 0.6315789473684211, 0.5714285714285714,
         0.7567567567567567, 0.5945945945945946, 0.6190476190476191, 0.5945945945945946, 0.6666666666666665,
         0.7368421052631577, 0.6666666666666666, 0.4, 0.6875, 0.8461538461538461, 0.6666666666666667,
         0.7441860465116279, 0.7692307692307693, 0.4666666666666667, 0.6666666666666665, 0.625, 0.7272727272727273,
         0.6842105263157895, 0.7906976744186046, 0.5882352941176471, 0.6666666666666665, 0.55, 0.7741935483870968,
         0.6842105263157895, 0.5882352941176471, 0.6285714285714287, 0.6666666666666667, 0.7346938775510204,
         0.6500000000000001, 0.7222222222222223, 0.7, 0.5555555555555556, 0.6666666666666666, 0.5555555555555556,
         0.7333333333333333, 0.5806451612903226, 0.6666666666666666, 0.5294117647058824, 0.5945945945945946,
         0.6923076923076924, 0.6451612903225806, 0.5161290322580646, 0.6111111111111112, 0.5294117647058824,
         0.7647058823529411, 0.47058823529411764, 0.6896551724137931, 0.5294117647058824, 0.7096774193548386,
         0.7647058823529411, 0.631578947368421, 0.6470588235294117, 0.6486486486486486, 0.6363636363636364,
         0.6666666666666666, 0.5625, 0.7894736842105263, 0.6046511627906976, 0.761904761904762, 0.4864864864864864,
         0.7407407407407408, 0.6500000000000001, 0.6666666666666665, 0.7727272727272727, 0.6451612903225806,
         0.6285714285714287, 0.7567567567567567, 0.6285714285714287, 0.5925925925925926, 0.5789473684210527,
         0.7567567567567567, 0.5714285714285714, 0.6666666666666666]
import numpy as np
array = np.sort(array)
new_array = array[5:95]
print(new_array)
print(np.average(new_array))