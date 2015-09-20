angular.module('starter.controllers', [])


.controller('AppCtrl', function($scope, $http, $firebaseObject, $firebaseArray, $ionicActionSheet, $ionicModal, Items, Auth) {
    $scope.creditCard = {};
    $scope.amount = null;
    $scope.txid = null;
    $scope.locations={};
    $scope.locations.latitude = 0;
    $scope.locations.longitude = 0;
    $scope.positions = [];
    $scope.userType = {};
    $scope.userType.passanger = false;
    $scope.userType.rider = false;
    $scope.clicked = false;
    $scope.authData;
    $scope.positions2={};
    $scope.positions2.latitude = 0;
    $scope.positions2.longitude = 0;

  var vcard  = {
    firstName: 'Shiva',
    lastName: 'Kaushal',
    number: '4005519200000004',
    expirationDate: '08/16',
    amount: '0'
  },
  acard= {
    firstName: 'Tian',
    lastName: 'Yuan',
    number: '371449635398431',
    expirationDate: '08/16',
    amount: '0'
  },
  mcard = {
    firstName: 'Daniel',
    lastName: 'Scott',
    number: '5555555555554444',
    expirationDate: '08/16',
    amount: '0'
  }

  $scope.riders = [];

  var itemsRef = new Firebase("https://bookmywride.firebaseio.com/");
  var passanger = new Firebase("https://bookmywride.firebaseio.com/passanger");
  var rider= new Firebase("https://bookmywride.firebaseio.com/rider");



    var itemsObj = $firebaseObject(itemsRef);

    $scope.passanger = $firebaseArray(passanger);
    $scope.rider = $firebaseArray(rider);

$scope.passanger.$watch(function(event) {
  //console.log('I am being triggered', event);
  $scope.passanger = $firebaseArray(passanger);
  //console.log('passangr', $scope.passanger);
});

$scope.rider.$watch(function(event) {
  //console.log('I am being triggered', event);
  $scope.rider = $firebaseArray(rider);
  //console.log('rider', $scope.rider);
});

  function _getRiders () {

     $http.get('https://cryptic-oasis-6309.herokuapp.com/api/driver')
        .success(function (data) {
           $scope.riders = data;
           console.log(data);
        })
        .error(function (data) {
            //alert("Error: " + data);
        });
  }
  _getRiders();

  navigator.geolocation.getCurrentPosition(function(position){
        console.log('here are the position', position);
      $scope.locations.latitude = position.coords.latitude;
       $scope.locations.longitude = position.coords.longitude;
     }, onError);

$scope.savefbinfo  = function() {
 


   $scope.modallogin.hide();
    console.log($scope.userType);

    if($scope.userType.passanger == true) {
      
  $http.get('https://cryptic-oasis-6309.herokuapp.com/api/customer/' + $scope.authData.id)
   .success(function (data) {
         console.log('User exists');
        })
        .error(function (data) {

          $scope.passanger.$add({
        id: $scope.authData.id,
        userData: $scope.authData
       })


          var toSend_Customer= {
            "facebook_id": parseInt($scope.authData.id),
            "name": $scope.authData.displayName,
            "email": $scope.authData.email,
            "description": $scope.authData.description
          };

    $http.post('https://cryptic-oasis-6309.herokuapp.com/api/customer', toSend_Customer)
    .success(function (data, status, headers, config) {
      console.log('saving data', JSON.stringify(data), JSON.stringify(status));
    }).error(function (data, status, headers, config) {
        console.log('There was a problem posting your information' + JSON.stringify(data) + JSON.stringify(status));
    });
        });

    }

    if($scope.userType.rider== true) {
      console.log('lllllll',$scope.authData.id);
       $http.get('https://cryptic-oasis-6309.herokuapp.com/api/driver/' + $scope.authData.id)
   .success(function (data) {
         console.log('User exists', JSON.stringify(data));
        })
        .error(function (data) {
           $scope.rider.$add({
        id: $scope.authData.id,
        userData: $scope.authData
      })
   

     navigator.geolocation.getCurrentPosition(function(position){
        console.log('here are the position', position);
      $scope.locations.latitude = position.coords.latitude;
       $scope.locations.longitude = position.coords.longitude;
       if($scope.userType.rider== true) {
        var toSend_Driver= {
        "facebook_id": parseInt($scope.authData.id),
        "name": $scope.authData.displayName,
        "email": $scope.authData.email,
        "description": $scope.authData.description,
        "location": {
            "latitude": $scope.locations.latitude,
            "longitude": $scope.locations.longitude
        }
        }
        $http.post('https://cryptic-oasis-6309.herokuapp.com/api/driver', toSend_Driver)
        .success(function (data, status, headers, config) {
          console.log('saving data', data);
        }).error(function (data, status, headers, config) {
            console.log('There was a problem posting your information' + JSON.stringify(data) + JSON.stringify(status));
        });
       }

     }, onError);


    })

  }    
   
  }

$scope.login = function() {
  var ref = new Firebase("https://bookmywride.firebaseio.com/");
ref.authWithOAuthPopup("facebook", function(error, authData) {
  if (error) {
    console.log("Login Failed!", error);
  } else {
    // the access token will allow us to make Open Graph API calls
    console.log(authData.facebook.accessToken);
    console.log("Logged in as", authData);

    $scope.authData = authData.facebook; // This will display the user's name in our view
  $http.get('https://graph.facebook.com/me?fields=cover,gender,age_range,birthday&access_token=' + authData.facebook.accessToken)
        .success(function (data) {
         console.log("got it" + JSON.stringify(data));
        $scope.authData.cover = data.cover.source;
        $scope.authData.gender = data.gender;
        $scope.authData.age = data.age_range;
        $scope.authData.id = data.id;
        $scope.authData.birthday = data.birthday;
        $scope.authData.description = "Erlich Bachman is a a supremely confident and arrogant entrepreneur who founded an innovation incubator in his home after the purchase of his airfare collator Aviato.";

         console.log('kshdkjhdkjhsakjd', $scope.authData);
        })
        .error(function (data) {
            console.log("Error: " + JSON.stringify(data));
        });

  }
}, {
  scope: "email,user_birthday" // the permissions requested
});
};





  $scope.options = function (option) {
    $scope.option = option;
  }

   $ionicModal.fromTemplateUrl('templates/transactionComplete.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modallogin) {
      $scope.modallogin = modallogin;
      $scope.modallogin.show();
  });


   $ionicModal.fromTemplateUrl('templates/transactionDetails.html', { scope: $scope })
        .then(function (txDetails) {
            $scope.txDetails = txDetails;
        });

  function triggerEvent (nfcEvent) {
      $scope.tag = nfcEvent.tag;
      $scope.hideSheet();
      assignCard($scope.tag);
      //alert(JSON.stringify($scope.tag));

  }
    //document.addEventListener('deviceready', this.onDeviceReady, false);
  $scope.tapping = function(amount){
    $scope.amount = amount;
    nfc.addTagDiscoveredListener(triggerEvent,
      function () {
      $scope.hideSheet = $ionicActionSheet.show({
          buttons: [
       { text: '<center><b>You are going to pay $' + $scope.amount}
     ],
           titleText: '<center>Tap your card please.</center>'
        });
      },
      function (reason) {
        console.log("Error: " + reason);
      }
    );
  };

  $scope.verifyTxId = function (txid) {
      $scope.txid = txid;
      $http.get('https://flashpay.herokuapp.com/getinfo/' + $scope.txid)
        .success(function (data) {
            $scope.currentTx = data[0];
            $scope.txDetails.show();
        })
        .error(function (data) {
            alert("Error: " + data);
        });
  };

  var assignCard = function(tag) {
     if($scope.tag.id[0] == 33 && $scope.tag.id[1] == 34 && $scope.tag.id[2] == 35 && $scope.tag.id[3] == 36) {
        $scope.creditCard = vcard;
    }
    if($scope.tag.id[0] == 111 && $scope.tag.id[1] == 122 && $scope.tag.id[2] == 84 && $scope.tag.id[3] == 11) {
        $scope.creditCard = acard;
    }
    if($scope.tag.id[0] == 15 && $scope.tag.id[1] == -107 && $scope.tag.id[2] == -70 && $scope.tag.id[3] == -7) {
        $scope.creditCard = mcard;
    }
     $scope.creditCard.amount = $scope.amount;

    nfc.removeTagDiscoveredListener(triggerEvent, function (){
    }, function (error){});

       $http.post('https://flashpay.herokuapp.com/createPayment', $scope.creditCard)
    .success(function (data, status, headers, config) {
      $scope.modal.show();
    }).error(function (data, status, headers, config) {
        alert('There was a problem retrieving your information' + data+ status);
    });

  };

  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  $scope.doLogin = function (username, password) {
      if (username.toLowerCase() === "eric" && password.toLowerCase() === "1234") {
          $scope.modallogin.hide();
      } else {
          alert("Invalid password entered");
      }
  };

  $scope.closeTxDetails = function () {
      $scope.txDetails.hide();
  };

  $scope.justcheck = function(){    
    }



//////////////////////////
  $scope.useCurrentLocation = function() {
    navigator.geolocation.getCurrentPosition(onSuccess, onError, { enableHighAccuracy: true });
  }

      // onSuccess Callback
  // This method accepts a Position object, which contains the
  // current GPS coordinates
  //
  var onSuccess = function(position) {
    var url = "insert url";
      $scope.locations.latitude = position.coords.latitude;
   $scope.locations.longitude = position.coords.longitude;
      console.log('bla', $scope.locations.latitude);
      $scope.authData.startingPosition = $scope.locations;
      //$scope.location.lon = position.coords.longitude;
      $http({method: 'GET', url: url,
              params: {
          locationx : position.coords.latitude,
          locationy : position.coords.longitude}})
        .success(function(data, status, headers, config) {
          console.log('got my information3' +JSON.stringify(data));
        });
  };

  // onError Callback receives a PositionError object
  //
  function onError(error) {
      alert('code: '    + error.code    + '\n' +
            'message: ' + error.message + '\n');
  }

  $scope.$watch('locations', function (location) {
    console.log('here we go again', location);
  })

  $scope.callRiders = function(riders) {
    var selectedRiders = [];
    var url = 'url', scenic;

    for (var i = 0; i< $scope.riders.length; i++) {
      if($scope.riders[i].checked){
        selectedRiders.push($scope.riders[i]);
      }
    }

    if($scope.option == 'Economical') {
      scenic = false
    } else {
      scenic = true;
    };


    var toSend= {
    "name": $scope.authData.displayName,
    "scenic": scenic,
    "driver_facebook_id": selectedRiders[0].facebook_id,
    "customer_facebook_id": parseInt($scope.authData.id),
    "start": {
        "latitude": $scope.locations.latitude,
        "longitude": $scope.locations.longitude
    },
    "end": {
        "latitude": $scope.positions[0].lat,
        "longitude": $scope.positions[0].lng
    }
  };

   passanger.child('endLocations').set(toSend.end);

  console.log('here is to send for patching trip', toSend);
  $http.post('https://cryptic-oasis-6309.herokuapp.com/api/trip', toSend)
    .success(function (data, status, headers, config) {
      console.log('here is response', JSON.stringify(data), JSON.stringify(status));
    }).error(function (data, status, headers, config) {
        console.log('There was a problem retrieving your information', JSON.stringify(data), JSON.stringify(status));
    });
  };




$scope.driverObject;
 

  function _pickups() {
    $http.get('https://cryptic-oasis-6309.herokuapp.com/api/trip/driver/' + $scope.authData.id)
       .success(function (data) {
        $scope.driverObject = data;
        console.log('nnnnnnnnnn', data[0].start, data[0].end );
        // $scope.locations2 = data[0].start;
        $scope.positions2= $scope.passanger.endLocations;
        //$scope.positions2.longitude = data[0].end.longitude;
        console.log('can we ever meet again',data[0], $scope.positions2);

          $scope.passanger.forEach(function(item) {
            console.log('logginf', item, $scope.driverObject[0].customer_facebook_id);
        if(item.id && item.id == ($scope.driverObject[0].customer_facebook_id).toString()) {
          console.log('found', item.userData);
          $scope.xyz = item.userData;
         // alert(JSON.stringify($scope.xyz));
        }
      })
          
       })
       .error(function (data) {
           // alert("Error: " + data);
       });


 }
 $scope.$watch('authData.id', function(id) {
  if(id) {
  _pickups();
    
  }
 })
  


})

.controller('DashCtrl', function ($scope, $http, $ionicActionSheet, $ionicModal) {

  $scope.rideComplete = function() {
    $ionicActionSheet.show({
          buttons: [
       { text: '<center><b>Thanks for Riding'}
     ],
           titleText: '<center>You are going to pay $50</center>'
        });

  }

})

.controller('CustomerCtrl', function ($scope, $compile) {
 
 // $("map").on("tap",function(){
 //   $scope.addMarker();
 //  });  
  
  $scope.addMarker = function(event) {
    var ll = event.latLng;
    $scope.positions.push({lat:ll.lat(), lng: ll.lng()});
    console.log($scope.positions);
  }

  $scope.cities = {
    1: {position: [41.878113, -87.629798]},
    2: {position: [40.714352, -74.005973]},
    3: {position: [37.7699298, -122.4469157]},
    4: {position: [49.25, -123.1]},
    5: {position: [49.25, -123.1]}
  }
  $scope.getRadius = function(num) {
    return Math.sqrt(num) * 100;
  }

})

.controller('ChatsCtrl', function ($scope, Chats) {
    // With the new view caching in Ionic, Controllers are only called
    // when they are recreated or on app start, instead of every page change.
    // To listen for when this page is active (for example, to refresh data),
    // listen for the $ionicView.enter event:
    //
    $scope.$on('$ionicView.enter', function (e) {
        Chats.all(function (transactions) {
            $scope.chats = transactions;
        });
    });
})

.controller('ChatDetailCtrl', function ($scope, $stateParams, Chats) {
    Chats.all(function (transactions) {
        $scope.chats = transactions;
    });
})

.controller('AccountCtrl', function ($scope, Chats) {
    $scope.settings = {
        enableFriends: true
    };

    Chats.all(function (transactions) {
        $scope.chats = transactions;
    });

    //  http.$get('flashpay.herokuapp.com/createPayment', params)
})

.controller('TickerCtrl', function ($scope) {

    $scope.cookie = "yummy";

    $scope.ticker_msgs = [];

    // Enable pusher logging - don't include this in production
    Pusher.log = function (message) {
        if (window.console && window.console.log) {
            window.console.log(message);
        }
    };

    var pusher = new Pusher('991b4111cb90d8ba79f6', {
        encrypted: true
    });
    var channel = pusher.subscribe('test_channel');
    channel.bind('my_event', function (data) {
        $scope.ticker_msgs.push(data);
        $scope.$apply();
    });
    //  http.$get('flashpay.herokuapp.com/createPayment', params)
});
