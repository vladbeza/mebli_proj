function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(49.966498,36.323479),
          zoom: 16,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
        var myLatlng = new google.maps.LatLng(49.966498,36.323479);
        var marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
                title:"'. $xmladd .'"
  });
 }


google.maps.event.addDomListener(window, "load", initialize);