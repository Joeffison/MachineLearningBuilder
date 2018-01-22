function mlbUtilsService(FileSaver, Blob,
                         $timeout) {
  var service = this;

  service.replaceArray = function (list, newData) {
    list.length = 0;

    angular.forEach(newData, function (item) {
      list.push(item);
    });
  };

  service.stringToFile = function (content, filename) {
    var data = new Blob([content], {type: 'text/plain;charset=utf-8'});
    FileSaver.saveAs(data, filename);
  };

  service.prettyPrintJson = function (obj) {
    return angular.toJson(obj, 2);
  };

  service.activateTooltips = function () {
    $timeout(function () {
      angular.element('.tooltipped').tooltip({delay: 50});
    }, 1000);
  };

  return service;
}

angular.module('app')
  .factory('mlbUtilsService', ['FileSaver', 'Blob',
    '$timeout',
    mlbUtilsService]);
