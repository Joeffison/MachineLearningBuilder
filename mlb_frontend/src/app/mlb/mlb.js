function mlbCtrl(mlbModelService, mlbUtilsService, mlbConstants,
                 $timeout) {
  var vm = this;
  vm.title = mlbConstants.PROJECT_NAME;

  vm.uploadURL = mlbModelService.uploadURL;
  vm.downloadMLModel = mlbModelService.downloadMLModel;
  vm.downloadCreateModel = mlbModelService.downloadCreateModel;
  vm.downloadLoadModel = mlbModelService.downloadLoadModel;
  vm.printJson = mlbUtilsService.prettyPrintJson;
  vm.models = [];

  vm.chosenMLAlgorithm = {name: 'the algorithm of your choice', predictors: [], predictors_values: []};
  vm.chooseMLAlgorithm = function (model) {
    if(vm.models && model.predictors && angular.isArray(model.predictors)) {
      vm.chosenMLAlgorithm = model;

      if(!(vm.chosenMLAlgorithm.predictors_values && angular.isArray(vm.chosenMLAlgorithm.predictors_values) &&
        vm.chosenMLAlgorithm.predictors_values.length == vm.chosenMLAlgorithm.predictors.length)) {
        vm.chosenMLAlgorithm.predictors_values = [];
        angular.forEach(vm.chosenMLAlgorithm.predictors, function (item) {
          vm.chosenMLAlgorithm.predictors_values.push(undefined);
        });
      }
    }

    // The code below fixes the bug on Materialize Labels for dynamic filled form fields.
    $timeout(function () {
      Materialize.updateTextFields();
    }, 1000);
  };

  vm.predict = function () {
    mlbModelService.predict(vm.chosenMLAlgorithm.id, [vm.chosenMLAlgorithm.predictors_values],
      function (response) {
        Materialize.toast('Prediction: ' + response.data.target, 4000, 'rounded');
    });
  };

  vm.onSuccessCSVUpload = function (response) {
    updateModels(response.data);
  };

  vm.onErrorCSVUpload = function () {
    updateModels(mlbModelService.models);
  };

  function updateModels(newData) {
    mlbUtilsService.replaceArray(vm.models, newData);
    mlbUtilsService.activateTooltips();
    mlbUtilsService.activateModals();

    angular.forEach(vm.models, function (item) {
      item.downloadMLModel = mlbModelService.downloadMLModel(item);
    });
  }
}

angular.module('app')
  .controller('MlbController', ['mlbModelService', 'mlbUtilsService', 'mlbConstants',
    '$timeout',
    mlbCtrl]);
