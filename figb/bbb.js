import { Line } from '@antv/g2plot';

const data = [
 { year: '-4%' },
{ year: '    ', value: -0.10 },
{ year: '-2%' },
{ year: '', value: 0.15 },
{ year: '0%' },
{ year: ' ', value: 0.33},
{ year: '2%',},
{ year: '  ', value: 0.70},
{ year: '4%',},
{ year: '   ', value: 1.11 },
{ year: '6%',},

];

const line = new Line('container', {
  data,
  padding:[50,30,30,200],
  xField: 'year',
  yField: 'value',
  label: {
    style: {
      fill: 'red',
      opacity: 1,
      fontSize: 15
    },
  },
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
      style: {
        shadowBlur: 4,
        stroke: '#000',
        fill: 'red',
      },
    },
  },
  connectNulls:true,
});

line.render();
