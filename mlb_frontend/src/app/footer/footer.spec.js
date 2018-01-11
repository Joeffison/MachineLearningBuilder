describe('footer component', function () {
  beforeEach(module('app', function ($provide) {
    $provide.factory('mlbFooter', function () {
      return {
        templateUrl: 'app/footer/footer.html'
      };
    });
  }));
  /*
  it('should render \'FountainJS team\'', angular.mock.inject(function ($rootScope, $compile) {
    var element = $compile('<mlb-footer></mlb-footer>')($rootScope);
    $rootScope.$digest();
    var footer = element.find('a');
    expect(footer.html().trim()).toEqual('FountainJS team');
  }));
  */
});
