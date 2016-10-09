/**
 * Created by karenx on 10/9/16.
 */

function loadTrafficHeatMap(map) {
    $.ajax({
        url: "/api/lot/nearby",
        success: function (data, result) {
            var heatIndices = [];
            var llr = [];

            var json_data = JSON.parse(data);

            var keys = Object.keys(json_data);
            var values = keys.map(function(v) { return json_data[v]; });

            for (var i = 0; i < values.length; i++) {
                var lot = values[i];

                var collegeVenues = lot["categories"]["college"];
                for (var venueIndex = 0; venueIndex < collegeVenues.length; venueIndex++) {
                    var lat = collegeVenues[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = collegeVenues[venueIndex]["longitude"];
                    llr.push(lng);
                    var rad = collegeVenues[venueIndex]["check_ins"];
                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }

                var workVenues = lot["categories"]["work"];
                for (var venueIndex = 0; venueIndex < workVenues.length; venueIndex++) {
                    var lat = workVenues[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = workVenues[venueIndex]["longitude"];
                    llr.push(lng);
                    var rad = workVenues[venueIndex]["check_ins"];
                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }

                var nightlife = lot["categories"]["nightlife"];
                for (var venueIndex = 0; venueIndex < nightlife.length; venueIndex++) {
                    var lat = nightlife[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = nightlife[venueIndex]["longitude"];
                    llr.push(lng);
                    var rad = nightlife[venueIndex]["check_ins"];
                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }

                var foodLife = lot["categories"]["food"];
                for (var venueIndex = 0; venueIndex < foodLife.length; venueIndex++) {
                    var lat = foodLife[venueIndex]["latitude"];
                    llr.push(lat);
                    var lng = foodLife[venueIndex]["longitude"];
                    llr.push(lng);
                    var rad = foodLife[venueIndex]["check_ins"];
                    llr.push(rad);

                    heatIndices.push(llr);
                    llr = [];
                }
            }

            L.heatLayer(heatIndices, {radius: 15}).addTo(map);
        }

    });
}