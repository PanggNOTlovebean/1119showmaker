import { Line } from '@antv/g2plot';

const data = [
  { year: '0.3',  },
  { year: '', value: -0.12 },
  { year: '0.4', },
  { year: ' ', value: 0.11 },
  { year: '0.5',  },
  { year: '   ', value: 0.15 },
  { year: '0.6',  },
  { year: '    ', value: 0.07 },
  { year: '0.7',  },
  { year: '     ', value: 0.03 },
  { year: '0.8',  },

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
