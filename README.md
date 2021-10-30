## SELCON

Modularised Implementation of the SELCON subset selection method from the paper: <br>
**[Training Data Subset Selection for Regression with Controlled Generalization Error](https://arxiv.org/abs/2106.12491)** <br>
by Durga Sivasubramanian, Rishabh Iyer, Ganesh Ramakrishnan, Abir De

### Installation
You can install the package using <br>
`pip install selcon`

### Dependencies
To run this code fully, you'll need PyTorch (we're using version 1.4.0) and scikit-learn. We've been running our code in Python 3.7.

### Usage
SELCON package can be utilised in Linear Subset Selection or Deep Subset Selection methods as:

#### Linear
```
from SELCON.datasets import load_def_data, get_data
from SELCON.linear import Regression
```
`load_def_data` provides functionality for using the datasets used for the experiments in the paper (provided you have them available in the 'Dataset' directory)
```
reg = Regression()

# Converts specified numpy arrays to torch tensors (assuming data has been split previously)
X_trn, X_val, Y_trn, Y_val = get_data(x_train, x_val, y_train, y_val)
# Trains SELCON model for a subset fraction of 0.03 on the training subset (no fairness)
reg.train_model(X_trn, Y_trn, X_val, Y_val, fraction = 0.03)
# Return optimal subset indices
subset_idxs = reg.return_subset()

# Returns the optimal subset of the training data for further use
X_sub = X_trn[subset_idxs]
y_sub = Y_trn[subset_idxs]
```

#### Deep
```
from SELCON.datasets import load_def_data, get_data
from SELCON.deep import DeepSelection
```
```
reg = DeepSelection()

# Converts specified numpy arrays to torch tensors (assuming data has been split into train-val sets previously)
X_trn, X_val, Y_trn, Y_val = get_data(x_train, x_val, y_train, y_val)
# Trains SELCON model for a subset fraction of 0.03 on the training subset (with fairness)
reg.train_model_fair(X_trn, Y_trn, X_val, Y_val, fraction = 0.03)
# Return optimal subset indices
subset_idxs = reg.return_subset()

# Returns the optimal subset of the training data for further use
X_sub = X_trn[subset_idxs]
y_sub = Y_trn[subset_idxs]
```