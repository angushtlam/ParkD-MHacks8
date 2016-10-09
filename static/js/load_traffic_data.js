/**
 * Created by angus on 10/8/16.
 */

function loadAllTrafficDataMap(map) {
    $.ajax({
        url: "/api/lot/nearby",
        success: function (data, result) {
            var json_data = JSON.parse(data);

            var keys = Object.keys(json_data);
            var values = keys.map(function(v) { return json_data[v]; });

            for (var i = 0; i < values.length; i++) {
                var lot = values[i];

                var collegeVenues = lot["categories"]["college"];
                for (var venueIndex = 0; venueIndex < collegeVenues.length; venueIndex++) {
                    var lat = collegeVenues[venueIndex]["latitude"];
                    var lng = collegeVenues[venueIndex]["longitude"];
                    var rad = collegeVenues[venueIndex]["check_ins"];

                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'red',
                        fillColor: '#f03',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }

                var workVenues = lot["categories"]["work"];
                for (var venueIndex = 0; venueIndex < workVenues.length; venueIndex++) {
                    var lat = workVenues[venueIndex]["latitude"];
                    var lng = workVenues[venueIndex]["longitude"];
                    var rad = workVenues[venueIndex]["check_ins"];

                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'blue',
                        fillColor: '#70E9FF',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }

                var nightlife = lot["categories"]["nightlife"];
                for (var venueIndex = 0; venueIndex < nightlife.length; venueIndex++) {
                    var lat = nightlife[venueIndex]["latitude"];
                    var lng = nightlife[venueIndex]["longitude"];
                    var rad = nightlife[venueIndex]["check_ins"];

                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'green',
                        fillColor: '#74FF70',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }

                var foodLife = lot["categories"]["food"];
                for (var venueIndex = 0; venueIndex < foodLife.length; venueIndex++) {
                    var lat = foodLife[venueIndex]["latitude"];
                    var lng = foodLife[venueIndex]["longitude"];
                    var rad = foodLife[venueIndex]["check_ins"];

                    if (rad > 40) rad = 40;
                    else if (rad < 10) rad = 10;

                     L.circle([lat, lng], {
                        color: 'yellow',
                        fillColor: '#FFF520',
                        fillOpacity: 0.1,
                        radius: rad
                     }).addTo(map);
                }
            }
        }

    });
}