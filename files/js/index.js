const deckgl = new deck.DeckGL({
  mapboxApiAccessToken: '',
  mapStyle: 'https://free.tilehosting.com/styles/darkmatter/style.json?key=U0iNgiZKlYdwvgs9UPm1',
  longitude: -74.0060,
  latitude: 40.7128,
  zoom: 9,
  minZoom: 5,
  maxZoom: 15,
  pitch: 40.5
});

let data = null;

const OPTIONS = ['radius', 'coverage', 'upperPercentile'];

const COLOR_RANGE = [
  [1, 152, 189],
  [73, 227, 206],
  [216, 254, 181],
  [254, 237, 177],
  [254, 173, 84],
  [209, 55, 78]
];

const LIGHT_SETTINGS = {
  lightsPosition: [-0.144528, 49.739968, 8000, -3.807751, 54.104682, 8000],
  ambientRatio: 0.4,
  diffuseRatio: 0.6,
  specularRatio: 0.2,
  lightsStrength: [0.8, 0.0, 0.8, 0.0],
  numberOfLights: 2
};

OPTIONS.forEach(key => {
  document.getElementById(key).oninput = renderLayer;
});

function renderLayer () {
  const options = {};
  OPTIONS.forEach(key => {
    const value = document.getElementById(key).value;
    document.getElementById(key + '-value').innerHTML = value;
    options[key] = value;
  });

  const hexagonLayer = new deck.HexagonLayer({
    id: 'heatmap',
    colorRange: COLOR_RANGE,
    data,
    elevationRange: [0, 50],
    elevationScale: 250,
    extruded: true,
    getPosition: d => d,
    lightSettings: LIGHT_SETTINGS,
    opacity: 1,
    ...options
  });

  deckgl.setProps({
    layers: [hexagonLayer]
  });
}

d3.csv('https://raw.githubusercontent.com/youdymoo/ridesharing/master/data/center/tripData-center-complete.csv',
   (error, response) => {
  data = response.map(d => [Number(d.lng), Number(d.lat)]);
  renderLayer();
});

var updateVar = setInterval(updateData, 5000);
var dataSource = 'https://raw.githubusercontent.com/youdymoo/ridesharing/master/data/center/tripData-center-complete.csv'

function updateData() {
  if (dataSource == 'https://raw.githubusercontent.com/youdymoo/ridesharing/master/data/center/tripData-center-complete.csv') {
    dataSource = 'https://raw.githubusercontent.com/youdymoo/ridesharing/master/data/sandbox/NYCdata-center-complete.csv';
  } else {
    dataSource = 'https://raw.githubusercontent.com/youdymoo/ridesharing/master/data/center/tripData-center-complete.csv';
  }

    d3.csv(dataSource,
   (error, response) => {
  data = response.map(d => [Number(d.lng), Number(d.lat)]);
  renderLayer();
});
}