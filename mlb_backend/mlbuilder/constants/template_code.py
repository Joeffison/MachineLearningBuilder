# -*- coding: utf-8 -*-

template_model_creation = """
import pandas as pd
from sklearn.model_selection import train_test_split

{model_import}

from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

csv_file = "{csv_file}"
model_file = "{model_file}"
predictors = {predictors}
targets = {targets}

historical_data = pd.read_csv(csv_file)
pred_train, pred_test, tar_train, tar_test = train_test_split(historical_data[predictors], historical_data[targets],
                                                              test_size=.3)
if len(targets) == 1:
    tar_train = tar_train.values.ravel()
    tar_test = tar_test.values.ravel()
model = DecisionTreeClassifier().fit(pred_train, tar_train)

predictions = model.predict(pred_test)
# Analyze accuracy of prediction.
# Remember that the data is randomly split into training and test set, so the values below will change
# ever time you create a new model
print confusion_matrix(tar_test, predictions)
print accuracy_score(tar_test, predictions)

pickle.dump(model, open(model_file, "wb"))
"""

template_model_predictor = """
import pickle

import numpy as np

model_file = "{model_file}"
model = pickle.load(open(model_file, 'rb'))

# input_to_predict has to follow the order below:
# {predictors}
prediction = model.predict(np.array([input_to_predict]))
print prediction
"""
