var app = angular.module('campusmap', [
    'ngRoute',
    'ngResource',
    'mapControllers',
    // "mobile-angular-ui",
]);

app.config(function ($routeProvider, $httpProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/views/home.html',
        controller: 'HomeCtrl'
      })
      .when('/detail/:category', {
        templateUrl: 'static/views/detail.html',
        controller: 'DetailCtrl'
      })
      .when('/end/:start', {
        templateUrl: 'static/views/end_location.html',
        controller: 'EndLocationCtrl'
      })
      .when('/building', {
        templateUrl: 'static/views/building.html',
        controller: 'BuildingCtrl'
      })
      .when('/room/:building', {
        templateUrl: 'static/views/room.html',
        controller: 'RoomCtrl'
      })
      .when('/professor', {
        templateUrl: 'static/views/professor.html',
        controller: 'ProfessorCtrl'
      })
      .when('/map', {
        templateUrl: 'static/views/map.html',
        controller: 'MapCtrl'
      })
      .when('/entrance', {
        templateUrl: 'static/views/entrance.html',
        controller: 'EntranceCtrl'
      })       
      .when('/direction/:entrance', {
        templateUrl: 'static/views/direction.html',
        controller: 'DirectionCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });

})

