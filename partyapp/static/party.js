angular
    .module('PartyApp', [])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: '../static/party.html',
                controller: 'PartyController'
            })
            .when('/secondPage', {
                templateUrl: '../static/secondPage.html',
                controller: 'SecondController'
            })
            .otherwise({ redirectTo: '/' });
    }])
    .factory('windowAlert', [
        '$window',
        function($window) {
            return $window.alert;
        }
    ])
    .controller('PartyController', [
        '$scope',
        '$http',
        'windowAlert',
        function($scope, $http, windowAlert) {
            $scope.RETRIEVE_DEFAULT_NR = 5;
            $scope.state = {};
            $scope.state.partyList = [];
            $scope.state.retrieveNr = $scope.RETRIEVE_DEFAULT_NR;
            $scope.state.pageName = 'partyList';

            $scope.addItem = function() {
                if (!$scope.state.newItem) {
                    windowAlert("text field must be non-empty");
                } else {
                    $http
                        .post('/partyAdd', {
                            item: $scope.state.newItem
                        })
                        .success(function(data, status, headers, config) {
                            if (data.success) {
                                $scope.retrieveCategory(
                                    $scope.state.retrieveNr
                                );
                            } else {
                                windowAlert('Adding of item failed');
                            }
                        })
                        .error(function(data, status, headers, config) {
                        });
                }
            };

            $scope.retrieveCategory = function(n) {
                $http
                    .get('/partyRetrieve/' + n)
                    .success(function(data, status, headers, config) {
                        if (data.success) {
                            $scope.state.partyList = data.partyList;
                        } else {
                            windowAlert('Retrieval failed');
                        }
                    })
                    .error(function(data, status, headers, config) {
                        windowAlert("Retrieval failed");
                    });
            };

            $scope.setAndRetrieveCategory = function(n) {
                $scope.state.retrieveNr = n;
                $scope.retrieveCategory($scope.state.retrieveNr);
            };
        }
    ])
    .directive('navtabs', function() {
        return {
            restrict: 'E',
            replace: true,
            templateUrl: '../static/navtabs.html',
            scope: {
                pageName: '='
            },
            controller: [
                '$scope',
                function($scope) {
                    this.selectTabIfOnPage = function(tab) {
                        if (tab.name === $scope.pageName) {
                            tab.selected = true;
                        }
                    };
                }
            ]
        };
    })
    .directive('tab', function() {
        return {
            require: '^navtabs',
            restrict: 'E',
            replace: true,
            transclude: true,
            scope: {},
            template: '<li ng-class="{ active: selected }"><a href="{{ href }}" ng-transclude></a></li>',
            link: function(scope, element, attr, navtabsCtrl) {
                scope.name = attr.name;
                scope.href = attr.href;
                scope.selected = false;
                navtabsCtrl.selectTabIfOnPage(scope);
            }
        };
    })
    .controller('SecondController', [
        '$scope',
        function($scope) {
            $scope.state = {};
            $scope.state.pageName = 'secondPage';
        }
    ])
    /*.controller('CategoryController', [
        '$scope',
        function($scope) {
            $scope.state = [
                {name: 'Food'},
                {name: 'Beverages'},
                {name: 'Miscellaneous'}];
            $scope.toggleActive = function(s){
                s.active = !s.active
            }
        ])*/
    ;
