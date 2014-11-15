var mapControllers = angular.module('mapControllers', []);

var START = '';
var BUILDING = '';
var ROOM = '';
var CATEGORY = {'parking': 'Parking Lot', 'busstop': 'Bus Stop', 'residence': 'Residence Hall',
                'building': 'Academic Building', 'venue': 'Venue'}
var ENTRANCE = {'N': 'North', 'S': 'South', 'E': 'East', 'W': 'West', 'NE': 'North East', 'SE': 'South East'}
var DIRECTIONS;

mapControllers.controller('HomeCtrl', function ($scope, $http, $routeParams) {
  ROOM = '';
  $scope.home = localStorage.getItem("home");

  $scope.hasHome = function() {
    return ($scope.home ? true : false);
  };

  // $scope.hasAlert = function() {
  //   return ALERT;
  // };
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
  $scope.start = START;
});

mapControllers.controller('BuildingCtrl', function ($scope, $http) {
  $http.get('static/scripts/location.json').success (function(data){
    $scope.buildings = data['destination'];
    $scope.start = START;
  });
});

mapControllers.controller('RoomCtrl', function ($scope, $http, $location, $routeParams) {
  BUILDING = $routeParams['building'];
  $scope.room;
  $scope.start = START;

  $http.get('../api/v1/rooms/' + BUILDING).success(function(data) {
    $scope.rooms = data.rooms;

    // Make sure the use input is a valid room number
    $scope.valid = function() {
      return (($scope.rooms.indexOf($scope.room) != -1) ? true : false);
    };

    $scope.invalid = function() {
      return (($scope.rooms.indexOf($scope.room) == -1 && $scope.room) ? true : false);
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
    $scope.start = START;
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
    $scope.start = START;
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

  $http.get('../api/v1/direction/' + BUILDING +'/'+ ROOM).success(function(data) {
    DIRECTIONS = data.direction;
  });
  
  $scope.trustSrc = function(src) {
    return $sce.trustAsResourceUrl(src);
  };

  $scope.hasRoom = function() {
    return (ROOM != "");
  };
});

mapControllers.controller('EntranceCtrl', function ($scope, $http) {
  $scope.building = BUILDING;
  $scope.direction = DIRECTIONS;

  $scope.getEntrance = function(d) {
    return ENTRANCE[d['entrance']];
  };
});

mapControllers.controller('DirectionCtrl', function ($scope, $http, $routeParams) { 
  for (i in DIRECTIONS) {
    if (DIRECTIONS[i]['entrance'] == $routeParams['entrance']) {
      $scope.direction = DIRECTIONS[i]['direction'];
    }
  }
  $scope.building = BUILDING;
  $scope.room = ROOM;
});

mapControllers.controller('SettingsCtrl', function ($scope, $http, $location) {
  $scope.hasHome = function() {
    return (localStorage.getItem('home') ? true : false);
  };

  $scope.reset = function() {
    localStorage.setItem("home", '');
    $location.path('/');
  };
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

