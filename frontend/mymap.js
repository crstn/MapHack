var mymap = L.map('map')
  .setView([55.676111, 12.568333], 13)
  .addLayer(L.tileLayer(
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: 'Map data © \
                  <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    }));

function onMapClick(e) {
  alert("You clicked the map at " + e.latlng);
}

mymap.on('click', onMapClick);
