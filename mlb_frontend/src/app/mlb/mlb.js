function mlbCtrl(FileSaver, Blob, $scope, $http) {
  $scope.title = "Machine Learning Builder";

  $scope.uploadURL = 'http://127.0.0.1:8000/mlbuilder/upload/csv/';
  $scope.mlPlan = {
    username: "trial",
    plan: ["classification"]
  };

  $scope.models = [];

  $scope.onSuccessCSVUpload = function (response) {
    $scope.models.length = 0;
    angular.forEach(response.data.models, function (item) {
      $scope.models.push(item);
    });
  };

  $scope.onModelSelected = function(model) {
    var data = new Blob([model.code_create_model], { type: 'text/plain;charset=utf-8' });
    FileSaver.saveAs(data, 'code_create_model.py');
  };

  function prettyPrintJson(json) {
    return JSON ? JSON.stringify(json, null, '  ') : 'your browser doesnt support JSON so cant pretty print';
  }

}

angular.module('app')
  .controller('mlbCtrl', ['FileSaver', 'Blob', '$scope', '$http', mlbCtrl]);
