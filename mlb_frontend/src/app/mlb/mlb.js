function mlbCtrl(mlbModelService, mlbUtilsService, mlbConstants,
                 $scope) {
  $scope.title = mlbConstants.project_name;

  $scope.uploadURL = mlbModelService.uploadURL;
  $scope.downloadMLModel = mlbModelService.downloadMLModel;
  $scope.downloadCreateModel = mlbModelService.downloadCreateModel;
  $scope.downloadLoadModel = mlbModelService.downloadLoadModel;

  $scope.models = [];
  $scope.onSuccessCSVUpload = function(response) {
    mlbUtilsService.replaceArray($scope.models, response.data.models);
    mlbUtilsService.activateTooltips();
  };

}

angular.module("app")
  .controller("mlbCtrl", ["mlbModelService", "mlbUtilsService", "mlbConstants",
    "$scope",
    mlbCtrl]);
