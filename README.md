# Machine Learning Builder
New to Machine Learning algorithms? Use this to evaluate different models using your own data and get the resulting code!!

> MLBuilder is a cloud-enabled, mobile-ready,
> AngularJS powered HTML5 platform helping
> beginners in Data Science to start learning and
> building their own ML solutions.


# New Features!
- Export the model of your choice and the Python Script to load it and run predictions!
- Export a Python Script that you can use to recreate the model<sup>[[1]](#footnote1)</sup> for any of the Machine Learning Algorithms

You can also:
- Import a CSV file and watch MLBuilder magically show you the accuracy metrics for the [models created](#machine-learning-algorithms-implemented) using your data.


### Tutorial

1. Access the [homepage]<sup>[[2]](#footnote2)</sup>

![MLBuilder Homepage][IMG Homepage]

2. Click on "Get Started"
3. Upload CSV File<sup>[[1]](#footnote1)</sup>

![MLBuilder Homepage][IMG Model Results]

4. Hover your cursor over the menu button for the model of your choice ![Menu Button][IMG Menu Button]
5. Click on the button to download the model ![Menu Button][IMG Download Model]
6. Click on the button to download the Python Script to Load/Use the model ![Menu Button][IMG Download Script Load Model]
    - Edit "model_file" in this file with the path to your model from step 5
    - Edit "input_to_predict" with values to make your predictions (as explained in the comments above the code)
7. Have fun making predictions!


### Technologies

- [AngularJs (Angular 1)][AngularJs] for the frontend
    - [JavaScript]
    - [HTML5]
    - [CSS3]
    - [Materialize] - Framework based on Material Design by Google
- [Django] ([Python]) for the backend
    - [Django Rest Framework][django-rest-framework] for a RESTful API
- [Scikit-learn (Sklearn)][scikit-learn] - Machine Learning Python Library
- [Pandas] - Python Data Analysis Library
- [NumPy] - Python Package for scientific computing
- Directives and other libraries listed as dependencies
 
And of course MLBuilder itself is open source with a [public repository][git-repo] on GitHub.


### Machine Learning Algorithms Implemented
- [Decision Tree]
- [Random Forest]
- [Logistic Regression]
- [Gaussian Naive Bayes]


### Installation

MLBuilder requires [Node.js] and [Bower] as well as Python (with pip) to run.

Clone the repository.

```sh
$ git clone https://github.com/Joeffison/MachineLearningBuilder.git
$ cd MachineLearningBuilder
```

Install the dependencies and start the backend server.

```sh
$ cd mlb_backend
$ pip install -r requirements.txt
$ python manage.py runserver
```

Install the dependencies and start the frontend server.

```sh
$ cd ..
$ cd mlb_frontend
$ npm install
$ bower install
$ npm run serve
```


### What's next?

 - Write MORE Tests
 - Run real-time predictions with any model
 - Implement feature for running Regression analysis
 - User Profiles (optional storage of data and models)
 - Implement more sophisticated ML algorithms
 - Helpers for Feature Engineering
 - Automation for creating charts with the uploaded data


### License
----
[MIT][license]


**Free and Open Source Software!**


[//]: # (Referenced links)
[homepage]: <https://joeffison.github.io/MachineLearningBuilder/>
[git-repo]: <https://github.com/Joeffison/MachineLearningBuilder>

[AngularJS]: <http://angularjs.org>
[js]: <https://www.javascript.com>
[javascript]: <https://www.javascript.com>
[html5]: <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5>
[css3]: <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3>
[materialize]: <http://materializecss.com/about.html>
[django]: <https://www.djangoproject.com/>
[python]: <https://www.python.org/>
[django-rest-framework]: <http://www.django-rest-framework.org>
[scikit-learn]: <http://scikit-learn.org/stable/>
[pandas]: <https://pandas.pydata.org/>
[numpy]: <http://www.numpy.org>
[node.js]: <http://nodejs.org>
[bower]: <https://bower.io/>
[Gulp]: <http://gulpjs.com>

[Decision Tree]: <https://www.r-bloggers.com/using-decision-trees-to-predict-infant-birth-weights/>
[Random Forest]: <https://www.r-bloggers.com/random-forests-in-r/>
[Logistic Regression]: <https://www.r-bloggers.com/how-to-perform-a-logistic-regression-in-r/>
[Gaussian Naive Bayes]: <https://machinelearningmastery.com/naive-bayes-for-machine-learning/>

[license]: <https://github.com/Joeffison/MachineLearningBuilder/blob/master/LICENSE>

[paper tsanas parkinson]: <http://ieeexplore.ieee.org/document/6678640/>
[paper-data tsanas parkinson]: <https://archive.ics.uci.edu/ml/datasets/LSVT+Voice+Rehabilitation>
[paper-data-preprocessed tsanas parkinson]: <https://github.com/Joeffison/MachineLearningBuilder/blob/master/docs/mock_data/LSVT_voice_rehabilitation.csv>

[//]: # (Referenced Images)
[IMG Homepage]: <https://github.com/Joeffison/MachineLearningBuilder/raw/development/docs/img/mlb_page_home.png>
[IMG Model Results]: <https://github.com/Joeffison/MachineLearningBuilder/raw/development/docs/img/mlb_page_models_results.png>
[IMG Menu Button]: <https://github.com/Joeffison/MachineLearningBuilder/raw/development/docs/img/mlb_btn_menu.png>
[IMG Download Model]: <https://github.com/Joeffison/MachineLearningBuilder/raw/development/docs/img/mlb_btn_download_model.png>
[IMG Download Script Load Model]: <https://github.com/Joeffison/MachineLearningBuilder/raw/development/docs/img/mlb_btn_download_code_load_model.png>

[//]: # (Footnotes)

----
<a name="footnote1"></a><sub>1.</sub> Every time a new model is created (either by rerunning MLBuilder for your data or by using the optional Python Script for recreating a particular model), the model will be potentially different (resulting in different predictions and consequently different accuracy results)

<a name="footnote2"></a><sub>2.</sub> Keep in mind that there is no public Backend Server running yet, thus all data and models showed were previously uploaded (MLBuilder generated based on real data from a paper<sup>[[3]](#footnote3)</sup> published by the MIT and the universities of Oxford and Colorado). An alternative is to run your own build of this project (locally or not) to create models on your data.

<a name="footnote3"></a><sub>3.</sub> A. Tsanas, M.A. Little, C. Fox, L.O. Ramig: Objective Automatic Assessment of Rehabilitative Speech Treatment in Parkinson's Disease, [IEEE Transactions on Neural Systems and Rehabilitation Engineering, Vol. 22, pp. 181-190][paper tsanas parkinson], January 2014. The data is available [here][paper-data tsanas parkinson] and the preprocessed data [here][paper-data-preprocessed tsanas parkinson].

