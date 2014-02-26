var width = 960, height = 800;

var color = d3.scale.category20();

var force = d3.layout.force().charge(-120).linkDistance(100).size([width, height]);

var svg = d3.select("body").append("svg").attr("width", width).attr("height", height);

function shadeColor(color, percent) {

	var R = parseInt(color.substring(1, 3), 16);
	var G = parseInt(color.substring(3, 5), 16);
	var B = parseInt(color.substring(5, 7), 16);

	R = ((R < 255) ? R : 255).toString(16);
	R = R.length == 1 ? "0" + R : R;
	G = ((G < 255) ? G : 255).toString(16);
	G = G.length == 1 ? "0" + G : G;
	B = ((B < 255) ? B : 255).toString(16);
	B = B.length == 1 ? "0" + B : B;

	return "#" + R + G + B;
}


$(".node").hover(function() {
	$(this).append("title").text(function(d) {
		return d.name + "over";
	});
});

d3.json("/media/code/data/a-song-of-ice-and-fire.json", function(error, graph) {
	force.nodes(graph.nodes).links(graph.links).start();

	var link = svg.selectAll(".link").data(graph.links).enter().append("line").attr("class", "link");

	var node = svg.selectAll(".node").data(graph.nodes).enter().append("circle").attr("class", "node").attr("r", function(d) {
		return 5 + 5 * Math.log(d.degree);
	}).style("fill", function(d) {
		return color(d.group);
	}).call(force.drag);

	node.append("title").text(function(d) {
		return d.name;
	});

	force.on("tick", function() {
		link.attr("x1", function(d) {
			return d.source.x;
		}).attr("y1", function(d) {
			return d.source.y;
		}).attr("x2", function(d) {
			return d.target.x;
		}).attr("y2", function(d) {
			return d.target.y;
		});

		node.attr("cx", function(d) {
			return d.x;
		}).attr("cy", function(d) {
			return d.y;
		});
	});
});
