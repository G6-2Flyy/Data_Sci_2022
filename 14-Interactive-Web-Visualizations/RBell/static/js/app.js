var data = {} ;

async function main() {
    input_data = await d3.json("samples.json");
    console.log(input_data)
    data = input_data;

    createDropdown();
    createBar("940");
    createMeta("940");
    createBubbles("940");
    createGauge("940");
};
main()

  
function createDropdown() {
    for (let i = 0; i < data.names.length; i++){
      let subjectID = data.names[i];
      d3.select("#selDataset").append("option").text(subjectID);
    }
  }

  function optionChanged(val) {
    createBar(val);
    createMeta(val);
    createBubbles(val);
    createGauge(val);
  }
  
  function createBar(val) {
    var data_bar = data.samples.filter(x => x.id === val)[0];
  
    var trace1 = {
      x: data_bar .sample_values.slice(0, 10).reverse(),
      y: data_bar .otu_ids.slice(0, 10).reverse().map(x => `OTU ID: ${x}`),
      name: 'Bacteria',
      type: 'bar',
      orientation: "h",
      hovertext: data_bar.otu_labels,
        marker: {
            color: 'teal',
        line: {
            color: 'yellow',
            width: 3.0
          }
        },
       
    }
  
    var traces = [trace1];
  
    var layout = {title: '<b> Top 10 Bacteria Per Subject </b>',  margin:{
        l:150 , t:35
    }};
  
    Plotly.newPlot('bar', traces, layout);
  }

  function createMeta(val) {
    var meta_data = data.metadata.filter(x => x.id == val)[0];
    console.log(meta_data);
    d3.select("#sample-metadata").html("");
    Object.entries(meta_data).forEach(function (key) {
      d3.select("#sample-metadata").append("p").text(`${key[0]}: ${key[1]}`);
    });
  }

  function createBubbles(val) {
    var bubble_data = data.samples.filter(x => x.id === val)[0];
  
    var trace1 = {
      x: bubble_data.otu_ids,
      y: bubble_data.sample_values,
      name: 'Bacteria',
      mode: 'markers',
      marker: {
        color: ['rgb(46,139,87)', 'rgb(255,255,0)',  'rgb(220,20,60)', 'rgb(0,128,128)'],
        size: bubble_data.sample_values
      },
      hovertext: bubble_data.otu_labels
    };
  
    var traces = [trace1];
  
    var layout = {title: '<b> Bacteria Per Subject Sample </b>'};
  
    Plotly.newPlot('bubble', traces, layout);
  }

function createGauge(val) {
    var gauge_data = data.metadata.filter(x => x.id == val)[0];
    console.log(gauge_data)
    d3.select("#gauge").html("");
    if(gauge_data.wfreq) {
    var graph_data = [
        {
          domain: { x: [0, 1], y: [0, 1] },
          value: gauge_data.wfreq,
          title: "<b> Belly Button Washing Frequency </b> <br> Scrubs per Week ",
          type: "indicator",
          mode: "gauge+number",
          gauge: {
            axis: { range: [null, 9], tickwidth: 1, tickcolor: "#800000" },
            steps: [
              { range: [0, 1], color: "#F0E68C" },
              { range: [1, 2], color: "#FFFF00" },
              { range: [2, 3], color: "#9ACD32"},
              { range: [3, 4], color: "#ADFF2F"},
              { range: [4, 5], color: "#7CFC00"},
              { range: [5, 6], color: "#32CD32"},
              { range: [6, 7], color: "#FA8072"},
              { range: [7, 8], color: "#FF6347"},
              { range: [8, 9], color: "#FF0000"},
            ],
            threshold: {
              line: { color: "red", width: 4 },
              thickness: 0.75,
              value: 490
            }
          }
        }
      ];
      
      var layout = { width: 400, height: 250, margin: { t: 15, b: 0 } };
      Plotly.newPlot('gauge', graph_data, layout);
    }
};