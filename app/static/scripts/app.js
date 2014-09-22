var app = angular.module('campusmap', [
    'ngRoute',
    'ngResource',
    'mapControllers',
]);

app.config(function ($routeProvider, $httpProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/views/home.html',
        controller: 'DirectionCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });

})

