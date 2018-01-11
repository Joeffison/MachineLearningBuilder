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
      template: '<h3>We are going to place a page where you can evaluate some ML models here.</h3>'
    });
}
