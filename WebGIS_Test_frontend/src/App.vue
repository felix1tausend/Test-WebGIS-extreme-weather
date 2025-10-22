<script setup>
import { ref, onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

var map
var osm
var dresdenMitte
var baseMaps
var overlayMaps 
var layerControl



onMounted(() => {

  osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap contributors'
  });
  dresdenMitte = L.marker([51.0557, 13.7274]);

map = L.map('map',{
  center: [51.0557, 13.7274],
  zoom: 12,
  layers: [osm],
  zoomControl: false, 
});


baseMaps = { "OSM": osm};
overlayMaps ={ "Station Dresden": dresdenMitte};

layerControl = L.control.layers(baseMaps, overlayMaps).addTo(map);
L.control.zoom({position: 'bottomright'}).addTo(map);


})

</script>




<template>
  <div class="z-0 relative w-full h-full flex justify-center items-center bg-gray-800">
    <!-- map -->
    <div id="map" class="z-10 w-full h-full"></div>
  </div>
</template>


