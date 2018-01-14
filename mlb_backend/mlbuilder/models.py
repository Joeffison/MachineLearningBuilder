# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sklearn.metrics import accuracy_score, confusion_matrix

# Create your models here.
class MLModel(models.Model):
    def __init__(self, name, model, pred_test, tar_test):
        self.name = name
        predictions = model.predict(pred_test)
        # Analyze accuracy of predictions
        self.confusion_matrix = confusion_matrix(tar_test, predictions)
        self.accuracy_score = accuracy_score(tar_test, predictions)

    def to_json(self):
        return {
            "name": self.name,
            #"confusion_matrix": self.confusion_matrix,
            "accuracy_score": self.accuracy_score
        }
