var mapControllers = angular.module('mapControllers', []);

var START = '';
var BUILDING = '';
var ROOM = '';
var CATEGORY = {'parking': 'Parking Lot', 'busstop': 'Bus Stop', 'residence': 'Residence Hall',
                'building': 'Academic Building', 'venue': 'Venue'}

mapControllers.controller('HomeCtrl', function ($scope, $http) {
  ROOM = '';
  $scope.home = localStorage.getItem("home");
});

mapControllers.controller('DetailCtrl', function ($scope, $http, $routeParams) {
  $http.get('static/scripts/location.json').success (function(data){
    $scope.category = data[$routeParams['category']];
    $scope.name = CATEGORY[$routeParams['category']];
  });

});

mapControllers.controller('EndLocationCtrl', function ($scope, $http, $routeParams) {
  // Set starting location to global variable.
  START = $routeParams['start'];
});

mapControllers.controller('BuildingCtrl', function ($scope, $http) {
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

    $scope.valid2 = function() {
      if ($scope.rooms.indexOf($scope.room) != -1 || !$scope.room) {
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

mapControllers.controller('ProfessorCtrl', function ($scope, $http, $location) {
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

mapControllers.controller('OtherendCtrl', function ($scope, $http, $location, $routeParams) {
  $http.get('static/scripts/location.json').success (function(data){
    $scope.locations = data[$routeParams.category];
    $scope.name = CATEGORY[$routeParams['category']];
  });

  $scope.confirm = function(p) {
    var r = confirm(START + " to " + p);
    if (r == true) {
      BUILDING = p;
      $location.path('/map');
    }
  };
});

mapControllers.controller('MapCtrl', function ($scope, $http, $sce) {
  $http.get('static/scripts/map.json').success (function(data){
    $scope.map = "https://www.google.com/maps/embed/v1/directions?origin=" + data[START] + "&destination=" + 
                data[BUILDING] + "&mode=walking&key=AIzaSyBYo_55KJMWURTNCZ9JkhT2zp-dj1ucOC8";
  });
  
  $scope.trustSrc = function(src) {
    return $sce.trustAsResourceUrl(src);
  };

  $scope.hasRoom = function() {
    return (ROOM != "");
  };
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

mapControllers.controller('SettingsCtrl', function ($scope, $http, $location) {

});

mapControllers.controller('SettingsDetailCtrl', function ($scope, $http, $location, $routeParams) {
  $http.get('static/scripts/location.json').success (function(data){
    $scope.category = data[$routeParams['category']];
    $scope.name = CATEGORY[$routeParams['category']];
  });

  $scope.sethome = function(location) {
    localStorage.setItem("home", location);
    $location.path('/');
  };
});

// localstrage.getItem()
