<script setup>
import { onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

var map
var osm
var baseMaps
var overlayMaps 
var layerControl



onMounted(async() => {


  map = L.map('map',{
  center: [51.0557, 13.7274],
  zoom: 14,
  zoomControl: false, 
  });

  osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  
      // Daten vom Backend abrufen
      const response = await fetch('http://192.168.178.24:5000/api/testmesswert');
      const data = await response.json();

      console.log(data)


      const markerGroup = L.layerGroup();

    for (const item of data) {
      L.marker([item.lat, item.lng])
        .bindPopup(`<b>${item.name}</b><br>Tagesmaximaltemperatur: ${item.txk}`)
        .addTo(markerGroup);
    }

  markerGroup.addTo(map);
      
  


baseMaps = { "OSM": osm};
overlayMaps ={"Station Dresden Mitte": markerGroup};

layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map);
L.control.zoom({position: 'bottomright'}).addTo(map);


})

</script>


<template>
  <div id="div1" class="bg-gray-800 h-screen w-screen">
    <!-- map -->
  <div id="div2">
    <div id="map"></div>
  </div>
  </div>
</template>


