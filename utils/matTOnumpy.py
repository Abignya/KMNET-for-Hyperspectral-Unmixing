import numpy as np
import scipy.io

datasets=["indian_pines_gt","DC2","JasperRidge","Samson", "Sim1", "TinyApex", "Cuprite"]

#  used to get the varibles in each and individual dataset
for i in datasets:
    k = i + ".mat"
    mat_file = scipy.io.loadmat(k)
    var_names = [var for var in mat_file.keys() if not var.startswith("__")]
    print(f"Variables in {k}: {var_names}")

datasets = {
    'Indian_pines_gt': ['indian_pines_gt'],
    'DC2': ['Y', 'E', 'A', 'H', 'W', 'p', 'L', 'labels'],
    'JasperRidge': ['Y', 'E', 'A', 'H', 'W', 'L', 'p', 'labels'],
    'Samson': ['Y', 'E', 'A', 'H', 'W', 'L', 'p', 'labels'],
    'Sim1': ['Y', 'E', 'A', 'p', 'H', 'W', 'L', 'labels'],
    'TinyApex': ['Y', 'E', 'A', 'H', 'W', 'L', 'p', 'labels'],
    'Cuprite': ['X']
}

for dataset, var_names in datasets.items():
    mat_file = scipy.io.loadmat(dataset + '.mat')
    data = {}
    for var_name in var_names:
        data[var_name] = mat_file[var_name]
    np.save(dataset + '.npy', data)

