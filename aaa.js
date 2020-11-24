import { Line } from '@antv/g2plot';

const data = [
  { year: '0.3' },
  { year: '', value: -0.23 },
  { year: '0.4' },
  { year: ' ', value: 0.22},
  { year: '0.5',},
  { year: '  ', value: 0.28 },
  { year: '0.6',},
  { year: '   ', value: 0.14 },
  { year: '0.7',},
   { year:'    ', value: 0.06 },
  { year: '0.8',},
 
];

const line = new Line('container', {
  data,
  xField: 'year',
  yField: 'value',
  tooltip: {
  fields: ['year', 'y'],
  },
  label: {style: {
      fill: 'red',
      opacity: 1,
      fontSize: 15
    },},
  point: {
    size: 5,
    shape: 'diamond',
    style: {
      fill: 'white',
      stroke: '#5B8FF9',
      lineWidth: 2,
    },
  },
  tooltip: { showMarkers: false },
  state: {
    active: {
      
    },
  },
  connectNulls:true,
});

line.update({ "theme": { "styleSheet": { "brandColor": "#025DF4", "paletteQualitative10": ["#025DF4", "#DB6BCF", "#2498D1", "#BBBDE6", "#4045B2", "#21A97A", "#FF745A", "#007E99", "#FFA8A8", "#2391FF"], "paletteQualitative20": ["#025DF4", "#DB6BCF", "#2498D1", "#BBBDE6", "#4045B2", "#21A97A", "#FF745A", "#007E99", "#FFA8A8", "#2391FF", "#FFC328", "#A0DC2C", "#946DFF", "#626681", "#EB4185", "#CD8150", "#36BCCB", "#327039", "#803488", "#83BC99"] } } });
line.render();
