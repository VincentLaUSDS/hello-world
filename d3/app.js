var width = 500
var height = 500

var data = [
  [0, 0],
  [50, 50],
  [100, 200],
  [300, 100],
  [400, 600]
]

var xScale = d3.scaleLinear()
               .domain(d3.extent(data, d => d[0]))
               .range([0, width])

var yScale = d3.scaleLinear()
               .domain(d3.extent(data, d => d[1]))
               .range([height, 0])

d3.select("svg")
  .selectAll("circle")
  .data(data)
  .enter()
  .append("circle")
  .attr('cx', d => xScale(d[0]))
  .attr('cy', d => yScale(d[1]))
  .attr('r', () => Math.random() * 20 + 'px')
  .attr('fill', 'blue');
