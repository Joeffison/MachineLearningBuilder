# -*- coding: utf-8 -*-

decision_tree = {
    "description": "A decision tree is an algorithm that builds a flowchart like graph to illustrate the possible "
                   "outcomes of a decision. To build the tree, the algorithm first finds the variable that does the "
                   "best job of separating the data into two groups. "
                   "Then, it repeats the above step with the other variables. "
                   "This results in a tree graph, where each split represents a decision. "
                   "The algorithm chooses the splits such that the maximum number of observations are classified "
                   "correctly. The biggest advantage of a decision tree is that it is really intuitive and can be "
                   "understood even by people with no experience in the field.\n"
                   "https://www.r-bloggers.com/using-decision-trees-to-predict-infant-birth-weights/",
    "url": "https://www.r-bloggers.com/using-decision-trees-to-predict-infant-birth-weights/",
}

random_forest = {
    "description": "In Random Forests the idea is to decorrelate the several trees which are generated on the different"
                   " bootstrapped samples from training Data.And then we simply reduce the Variance in the Trees by "
                   "averaging them. Averaging the Trees helps us to reduce the variance and also improve the Perfomance"
                   " of Decision Trees on Test Set and eventually avoid Overfitting. The idea is to build lots of Trees"
                   " in such a way to make the Correlation between the Trees smaller.\n"
                   "https://www.r-bloggers.com/random-forests-in-r/",
    "url": "https://www.r-bloggers.com/random-forests-in-r/",
}

logistic_regression = {
    "description": 'Logistic regression is a method for fitting a regression curve, y = f(x), '
                   'when y is a categorical variable. The typical use of this model is '
                   'predicting y given a set of predictors x. The predictors can be continuous, categorical or a mix '
                   'of both. The categorical variable y, in general, can assume different values. '
                   'In the simplest case scenario y is binary meaning that it can assume either the value 1 or 0 '
                   '(“binomial logistic regression”), since the variable to predict is binary, however, '
                   'logistic regression can also be used to predict a dependent variable which can assume more '
                   'than 2 values (“multinomial logistic regression”).\n'
                   'https://www.r-bloggers.com/how-to-perform-a-logistic-regression-in-r/',
    "url": "https://www.r-bloggers.com/how-to-perform-a-logistic-regression-in-r/",
}

gaussian_naive_bayes = {
    "description": "Naive Bayes is a classification algorithm for binary (two-class) and multi-class "
                   "classification problems. It is called naive Bayes because the calculation of "
                   "the probabilities for each hypothesis are simplified to make their calculation tractable. "
                   "Rather than attempting to calculate the values of each attribute value P(d1, d2, d3|h), "
                   "they are assumed to be conditionally independent given the target value and calculated as "
                   "P(d1|h) * P(d2|H) and so on. This is a very strong assumption that is most unlikely in real data, "
                   "i.e. that the attributes do not interact. Nevertheless, the approach "
                   "performs surprisingly well on data where this assumption does not hold.\n"
                   "https://machinelearningmastery.com/naive-bayes-for-machine-learning/",
    "url": "https://machinelearningmastery.com/naive-bayes-for-machine-learning/",
}
