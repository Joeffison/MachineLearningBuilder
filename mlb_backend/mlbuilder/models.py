# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import pickle

from django.conf import settings
from django.core.files.storage import default_storage
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

        model_file = csv_file[:-3] + name + ".mlbuilder.model"

        self.code_create_model = template_code.template_model_creation.format(model_import=model_import,
                                                                              csv_file=csv_file, model_file=model_file,
                                                                              predictors=predictors, targets=targets)

        self.code_load_model = template_code.template_model_predictor.format(model_file=model_file,
                                                                             predictors=predictors)

        self.ml_model = model_file
        model_file = default_storage.open(model_file, "wb")
        pickle.dump(model, model_file)

    def to_json(self):
        return {
            "name": self.name,
            #"confusion_matrix": self.confusion_matrix,
            "accuracy_score": self.accuracy_score,
            "code_create_model": self.code_create_model,
            "code_load_model": self.code_load_model,
            "ml_model": self.ml_model,
        }
