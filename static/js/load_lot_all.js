/**
 * Created by angus on 10/8/16.
 */
var lotMarkerLayer = [];
var lotPopupLayer = [];

function loadAllLotMarkersOnLeafletMap(map) {
    $.ajax({
        url: "/api/lot/all",
        success: function (data, result) {
            var allLots = JSON.parse(data)["results"];

            if (lotMarkerLayer.length != 0) {
                map.removeLayer(lotMarkerLayer);
            }

            var sidebarHtml = "";
            var newMarkers = [];
            var newPopups = [];
            for (var i = 0; i < allLots.length; i++) {
                var lat = allLots[i]["latitude"];
                var long = allLots[i]["longitude"];
                newMarkers[i] = L.marker([lat, long]);
                newPopups[i] = L.popup()
                    .setLatLng([lat + 0.00075, long])
                    .setContent(allLots[i]["name"]);

                sidebarHtml += '<div class="lot-block">' +
                    '<div class="lot-name">' + allLots[i]["name"] + '</div>' +
                    '<div class="lot-location">' + allLots[i]["address"] + '</div>' +
                    '<div class="lot-status">' + allLots[i]["spaces"] + ' Spaces</div>' +
                    '</div>';
            }

            lotMarkerLayer = L.layerGroup(newMarkers).addTo(map);
            lotPopupLayer = L.layerGroup(newPopups).addTo(map);
            $("#sidebar-lots").html(sidebarHtml);

        }
    });
}