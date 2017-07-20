# D3 Introduction
Notes from session at Rithm school meetup on 2017-07-19

http://github.com/rithmschool/intro_to_d3

Objectives:
1. Bind data to elements (including elements that aren't on the page yet!)
2. Append new elements in the page that are tied to data
3. Scale your data to fit on the page
4. Create a scatterplot using `d3`

Need to go over some prerequisites:
1. How to use D3 to navigate and manipulate the DOM
2. Quick intro to SVG

`d3.select("p")`

Selects the first `p` element from the DOM.

An example of method chaining:
`d3.select("p").text("I've set text using D3").style("font-size", "100px")`

Can also pass in functions

`d3.selectAll('p').text(function(saveForLater, idx){return "I am the p tag at index " + idx}).style('font-size', '20px')`

## Let's Get some data in
```
var quotes = [
    "No crying in baseball",
    "This is the war room",
    "hello helloe"
]
```

Consider this chaining of functions. What's going on?

```
d3.select("body")
  .selectAll("p")
  .data(quotes)
  .enter()
  .append("p")
    .text(function(d) { return d;})
```

Let's break it down

1. `d3.select("body")`: selects the body element
2. `.selectAll("p")`: selects all p tags. In `index.html` there were no `p` tags, so it returns a NodeList of length 0. Without this, you'd be appending the new `p` tags outside the body.
3. `.data(quotes)`: binds data to elements.

So in this case data is length 3, element: length 0, enter: 3. This is somewhat d3 magic, d3 is creating 3 enter nodes.

4. `.enter()`: gives you access to the 3 nodes in the enter selection. 
5. `.append("p")`: Appends `p` tag
6. `.text(function(d) { return d;})`: sets text as each element in quotes.

Notice that in d3, a function can be both a getter and a setter. By that I mean that `.text` can either get text if it's there, or set the text if you give it an input (like what we did above).

Let's get into most basic example of data visualization

```
var quotes = [
    {text: "No crying in baseball", color: "red"},
    {text: "This is the war room", color: "blue"},
    {text: "hello helloe", color: "green"}
]
```

Now let's color each of these texts

```
d3.select("body")
  .selectAll("p")
  .data(quotes)
  .enter()
  .append("p")
    .text(function(d) { return d.text;})
    .style('color', function(d) {return d.color;})
```

This is an example of how we bind the DOM to data (color), so we can color the text.

## What is an SVG?
Scalable Vector Graphics. D3 works with SVG

Example:
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Our first d3 project</title>
  <style>
    body {
      text-align: center;
    }
  </style>
</head>
<body>
  <svg width="500" height="500">
    <circle
        cx="100"
        cy="100"
        r="100"
        fill="blue"
        stroke="green"
        stroke-width="10px"
    />
  </svg>
  <script src="https://d3js.org/d3.v4.js"></script>
</body>
</html>
```

## More advanced stuff with D3
```
var scale = d3.scaleLinear()
              .domain([0, 1])
              .range([-2, 7])
```

Scales data set of [0, 1] to [-2, 7]. 
