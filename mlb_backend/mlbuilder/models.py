# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sklearn.metrics import accuracy_score, confusion_matrix
import template_code

# Create your models here.
class MLModel(models.Model):
    def __init__(self, name, model, pred_test, tar_test, model_import, csv_file, predictors, targets):
        self.name = name
        predictions = model.predict(pred_test)
        # Analyze accuracy of predictions
        self.confusion_matrix = confusion_matrix(tar_test, predictions)
        self.accuracy_score = accuracy_score(tar_test, predictions)
        self.code_create_model = template_code.template_model_creation.format(model_import=model_import,
                                                                              csv_file=csv_file, predictors=predictors,
                                                                              targets=targets)
        self.code_load_model = template_code.template_model_predictor.format(csv_file=csv_file, predictors=predictors)

    def to_json(self):
        return {
            "name": self.name,
            #"confusion_matrix": self.confusion_matrix,
            "accuracy_score": self.accuracy_score,
            "code_create_model": self.code_create_model,
            "code_load_model": self.code_load_model,
        }
