var mapControllers = angular.module('mapControllers', []);

var START = '';
var BUILDING = '';
var ROOM = '';

mapControllers.controller('HomeCtrl', function ($scope, $http) {
  // Use param to show different lists
});

mapControllers.controller('DetailCtrl', function ($scope, $http, $routeParams) {
  $http.get('static/scripts/location.json').success (function(data){
    $scope.category = data[$routeParams['category']];
  });

});

mapControllers.controller('EndLocationCtrl', function ($scope, $http, $routeParams) {
  // Set starting location to global variable.
  START = $routeParams['start'];
});

mapControllers.controller('BuildingCtrl', function ($scope, $http, $routeParams) {
  $http.get('static/scripts/location.json').success (function(data){
    $scope.buildings = data['destination'];
  });
});

mapControllers.controller('RoomCtrl', function ($scope, $http, $location, $routeParams) {
  BUILDING = $routeParams['building'];
  $scope.room;

  $http.get('../api/v1/rooms/' + BUILDING).success(function(data) {
    $scope.rooms = data.rooms;

    // Make sure the use input is a valid room number
    $scope.valid = function() {
      if ($scope.rooms.indexOf($scope.room) != -1) {
        return true;
      }
      return false;  
    };
  });

  $scope.confirm = function () {
    var r = confirm(START + " to " + BUILDING + " " + $scope.room)
    if (r == true) {
      ROOM = $scope.room;
      $location.path('/map');
    }
  };

});

mapControllers.controller('ProfessorCtrl', function ($scope, $http, $location, $routeParams) {
  $http.get('../api/v1/professor').success(function(data) {
    $scope.professors = data.professors;
  });

  $scope.confirm = function(p) {
    var r = confirm(START + " to " + p[1] + " " + p[2]);
    if (r == true) {
      BUILDING = p[1];
      ROOM = p[2];
      $location.path('/map');
    }
  }; 
});


mapControllers.controller('MapCtrl', function ($scope, $http, $routeParams) {
  $scope.origin = "Lawther%20Hall%2C%20West%2023rd%20Street%2C%20Cedar%20Falls%2C%20IA";
  $scope.destination = "Innovative%20Teaching%20and%20Technical%20Center%2C%20Campus%20St%2C%20Cedar%20Falls%2C%20IA";
});

mapControllers.controller('EntranceCtrl', function ($scope, $http, $routeParams) {
  $scope.building = BUILDING;
  $http.get('../api/v1/entrance/' + $scope.building).success(function(data) {
    $scope.entrance = data.entrance;
  });  
});

mapControllers.controller('DirectionCtrl', function ($scope, $http, $routeParams) {
  $http.get('../api/v1/direction/' + BUILDING +'/'+ ROOM +'/'+ $routeParams.entrance).success(function(data) {
    $scope.direction = data.direction;
    $scope.building = BUILDING;
    $scope.room = ROOM;
  });

});




