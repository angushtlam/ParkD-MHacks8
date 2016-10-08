var map = null;

$(document).ready(function () {
    map = L.map("map").setView([userLat, userLong], 13);

    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        minZoom: 12,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    var circle = L.circle([userLat, userLong], {
        color: '#9F9A01',
        fillColor: '#9F9A01',
        fillOpacity: 0.05,
        radius: 5000
    }).addTo(map);

});