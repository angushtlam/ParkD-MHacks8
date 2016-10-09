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

                sidebarHtml += '<div class="lot-block" id="lot-block-' + i + '">' +
                    '<div class="lot-name">' + allLots[i]["name"] + '</div>' +
                    '<div class="lot-location">' + allLots[i]["address"] + '</div>' +
                    '<div class="lot-status">' + allLots[i]["spaces"] + ' Spaces</div>' +
                    '<div class="lot-data">' +
                        '<div class="lot-lat">' + allLots[i]["latitude"] + '</div>' +
                        '<div class="lot-long">' + allLots[i]["longitude"] + '</div>' +
                    '</div>' +
                    '</div>';

            }

            lotMarkerLayer = L.layerGroup(newMarkers).addTo(map);
            lotPopupLayer = L.layerGroup(newPopups).addTo(map);
            $("#sidebar-lots").html(sidebarHtml);

            // On click add behavior to "search" address in search bar
            for (var i = 0; i < allLots.length; i++) {
                $("#lot-block-" + i).click(function () {
                    var lat = parseFloat($(this).find(".lot-lat").html());
                    var long = parseFloat($(this).find(".lot-long").html());

                    $("#ui-search-bar").val($(this).find(".lot-location").html());
                    map.panTo(new L.LatLng(lat, long));
                });
            }
        }
    });
}