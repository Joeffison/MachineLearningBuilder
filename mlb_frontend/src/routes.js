angular
  .module('app')
  .config(routesConfig);

/** @ngInject */
function routesConfig($stateProvider, $urlRouterProvider, $locationProvider) {
  $locationProvider.html5Mode(true).hashPrefix('!');
  $urlRouterProvider.otherwise('/');

  $stateProvider
    .state('home', {
      url: '/',
      component: 'app'
    });

  $stateProvider
    .state('mlbuilder', {
      url: '/mlbuilder',
      templateUrl: 'app/mlb/mlb.html',
      controller: 'MlbController',
      controllerAs: 'vm'
    });
}
