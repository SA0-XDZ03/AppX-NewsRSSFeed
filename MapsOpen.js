const littleton = L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.'),
  denver = L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.'),
  aurora = L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.'),
  golden = L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.');
const cities = L.layerGroup([littleton, denver, aurora, golden]);
const street = L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
    maxZoom: 18
  }),
  watercolor = L.tileLayer('http://tile.stamen.com/watercolor/{z}/{x}/{y}.jpg', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
    maxZoom: 18
  });
const layerControl = L.map('layerControl', {
  center: [39.73, -104.99],
  zoom: 10,
  layers: [street, cities]
});
const baseMaps = {
  Street: street,
  Watercolor: watercolor
};
const overlayMaps = {
  Cities: cities
};
L.control.layers(baseMaps, overlayMaps).addTo(layerControl);
L.tileLayer('https://c.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
  maxZoom: 18
}).addTo(layerControl);