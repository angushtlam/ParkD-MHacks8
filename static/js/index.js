var map = null;

$(document).ready(function () {
    setUpLeaflet();
    loadAllLotMarkersOnLeafletMap(map);
    loadAllTrafficDataMap(map);
    loadTrafficHeatMap(map);
});

function setUpLeaflet() {
    map = L.map("map", {closePopupOnClick: false}).setView([userLat, userLong], 15);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        minZoom: 13,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
}