/**
 * Created by hch on 2017. 1. 22..
 */





class View_Result_header extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="result_header">
                <div className="container">
                    <h1 className="result_title">SAMSUNG</h1>
                    <h2 className="result_stock">▲1800000</h2>
                </div>
            </div>


        )
    }
}

class View_Result_content extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
            <div className="charts-container cf">
              <div className="chart" id="graph-1-container">
                <h2 className="title">Hours worked</h2>
                <div className="chart-svg">
                  <svg className="chart-line" id="chart-1" viewBox="0 0 80 40">
                    <defs>
                      <clipPath id="clip" x="0" y="0" width="80" height="40" >
                        <rect id="clip-rect" x="-80" y="0" width="77" height="38.7"/>
                      </clipPath>

                    <linearGradient id="gradient-1">
                        <stop offset="0" stop-color="#00d5bd" />
                        <stop offset="100" stop-color="#24c1ed" />
                    </linearGradient>

                    <linearGradient id="gradient-2">
                        <stop offset="0" stop-color="#954ce9" />
                        <stop offset="0.3" stop-color="#954ce9" />
                        <stop offset="0.6" stop-color="#24c1ed" />
                        <stop offset="1" stop-color="#24c1ed" />
                    </linearGradient>


                      <linearGradient id="gradient-3" x1="0%" y1="0%" x2="0%" y2="100%">>
                        <stop offset="0" stop-color="rgba(0, 213, 189, 1)" stop-opacity="0.07"/>
                        <stop offset="0.5" stop-color="rgba(0, 213, 189, 1)" stop-opacity="0.13"/>
                        <stop offset="1" stop-color="rgba(0, 213, 189, 1)" stop-opacity="0"/>
                    </linearGradient>


                    <linearGradient id="gradient-4" x1="0%" y1="0%" x2="0%" y2="100%">>
                        <stop offset="0" stop-color="rgba(149, 76, 233, 1)" stop-opacity="0.07"/>
                        <stop offset="0.5" stop-color="rgba(149, 76, 233, 1)" stop-opacity="0.13"/>
                        <stop offset="1" stop-color="rgba(149, 76, 233, 1)" stop-opacity="0"/>
                    </linearGradient>

                </defs>
                  </svg>
                  <h3 className="valueX">time</h3>
                </div>
                <div className="chart-values">
                  <p className="h-value">1689h</p>
                  <p className="percentage-value"></p>
                  <p className="total-gain"></p>
                </div>
                <div className="triangle green"></div>
              </div>
              <div className="chart" id="graph-2-container">
                <h2 className="title">Hours worked</h2>
                <div className="chart-svg">
                  <svg className="chart-line" id="chart-2" viewBox="0 0 80 40">
                  </svg>
                  <h3 className="valueX">time</h3>
                </div>
                <div className="chart-values">
                  <p className="h-value">322h</p>
                  <p className="percentage-value"></p>
                  <p className="total-gain"></p>
                </div>
                <div className="triangle red"></div>
              </div>
              <div className="chart circle" id="circle-1">
                <h2 className="title">IBApps Website</h2>
                <div className="chart-svg align-center">
                  <h2 className="circle-percentage"></h2>
                  <svg className="chart-circle" id="chart-3" width="50%" viewBox="0 0 100 100">
                    <path className="underlay" d="M5,50 A45,45,0 1 1 95,50 A45,45,0 1 1 5,50"/>
                  </svg>
                </div>
                <div className="triangle green"></div>
              </div>
              <div className="chart circle" id="circle-2">
                <h2 className="title">IBApps Website</h2>
                <div className="chart-svg align-center">
                  <h2 className="circle-percentage"></h2>
                  <svg className="chart-circle" id="chart-4" width="50%" viewBox="0 0 100 100">
                    <path className="underlay" d="M5,50 A45,45,0 1 1 95,50 A45,45,0 1 1 5,50"/>
                  </svg>
                </div>
                <div className="triangle red"></div>
              </div>
            </div>
            </div>


        )
    }
}

// class View_Result_content_chart extends React.component
// {
//     constructor(props)
  //  {/*{*/}
  //      {/*super(props);*/}
  //  {/*}*/}

   // {/*render()*/}
//     {
//         return (
//
//
//         );
//     }
// }

ReactDOM.render(<View_Result_header/>, document.getElementById('titleBar'));
ReactDOM.render(<View_Result_content/>, document.getElementById('content'));


var chart_h = 40;
var chart_w = 80;
var stepX = 77 / 14;


function point(x, y) {
    x: 0;
    y: 0;
}
/* DRAW GRID */
function drawGrid(graph) {
    var graph = Snap(graph);
    var g = graph.g();
    var i = 0 ;
    g.attr('id', 'grid');

    for ( i = 0; i <= stepX + 2; i++) {
        var horizontalLine = graph.path(
            "M" + 0 + "," + stepX * i + " " +
            "L" + 77 + "," + stepX * i);
        horizontalLine.attr('class', 'horizontal');
        g.add(horizontalLine);
    };
    for (i = 0; i <= 14; i++) {
        var horizontalLine = graph.path(
            "M" + stepX * i + "," + 38.7 + " " +
            "L" + stepX * i + "," + 0)
        horizontalLine.attr('class', 'vertical');
        g.add(horizontalLine);
    };
}
drawGrid('#chart-2');
drawGrid('#chart-1');

function drawLineGraph(graph, points, container, id) {
    var graph = Snap(graph);


    var i = 0;
    /*END DRAW GRID*/

    /* PARSE POINTS */

    var myPoints = [];
    var shadowPoints = [];

    function parseData(points) {
        for (i = 0; i < points.length; i++) {
            var p = new point();
            var pv = points[i] / 100 * 40;
            p.x = 83.7 / points.length * i + 1;
            p.y = 40 - pv;
            if (p.x > 78) {
                p.x = 78;
            }
            myPoints.push(p);
        }
    }
    var segments = [];


    function createSegments(p_array) {
        for (i = 0; i < p_array.length; i++) {
            var seg = "L" + p_array[i].x + "," + p_array[i].y;
            if (i === 0) {
                seg = "M" + p_array[i].x + "," + p_array[i].y;
            }
            segments.push(seg);
        }
    }

    function joinLine(segments_array, id) {
        var line = segments_array.join(" ");
        var line = graph.path(line);
        line.attr('id', 'graph-' + id);
        var lineLength = line.getTotalLength();
        line.attr({
            'stroke-dasharray': lineLength,
                'stroke-dashoffset': lineLength
        });

    }

    function calculatePercentage(points, graph) {
        var initValue = points[0];
        var endValue = points[points.length - 1];
        var sum = endValue - initValue;
        var prefix;
        var percentageGain;
        var stepCount = 1300 / sum;

        function findPrefix() {
            if (sum > 0) {
                prefix = "+";
            } else {
                prefix = "";
            }
        }
        var percentagePrefix = "";


        function percentageChange() {
            percentageGain = initValue / endValue * 100;

            if(percentageGain > 100){
                console.log('over100');
                percentageGain = Math.round(percentageGain * 100*10) / 100;
            }else if(percentageGain < 100){
                console.log('under100');
                percentageGain = Math.round(percentageGain * 10) / 10;
            }
            if (initValue > endValue) {
                percentageGain = endValue/initValue*100-100;

                percentageGain = percentageGain.toFixed(2);
                percentagePrefix = "";

                $(graph).find('.percentage-value').addClass('negative');
            } else {
                percentagePrefix = "+";
            }
            if(endValue > initValue){
                percentageGain = endValue/initValue*100;
                percentageGain = Math.round(percentageGain);
            }
        };
        percentageChange();
        findPrefix();
        var percentage = $(graph).find('.percentage-value');

        var totalGain = $(graph).find('.total-gain');
        var hVal = $(graph).find('.h-value');

        function count(graph, sum) {
            var totalGain = $(graph).find('.total-gain');
            var i = 0;
            var time = 1300;
            var intervalTime = Math.abs(time / sum);
            var timerID = 0;
            if (sum > 0) {
                var timerID = setInterval(function () {
                    i++;
                    totalGain.text(percentagePrefix + i);
                    if (i === sum) clearInterval(timerID);
                }, intervalTime);
            } else if (sum < 0) {
                var timerID = setInterval(function () {
                    i--;
                    totalGain.text(percentagePrefix + i);
                    if (i === sum) clearInterval(timerID);
                }, intervalTime);
            }
        }
        count(graph, sum);
        percentage.text(percentagePrefix + percentageGain + "%");

        totalGain.text("0%");
        setTimeout(function () {
            percentage.addClass('visible');
            hVal.addClass('visible');
        }, 1300);

    }


    function showValues() {
        var val1 = $(graph).find('.h-value');
        var val2 = $(graph).find('.percentage-value');
        val1.addClass('visible');
        val2.addClass('visible');
    }

    function drawPolygon(segments, id) {
        var lastel = segments[segments.length - 1];
        var polySeg = segments.slice();
        polySeg.push([78, 38.4], [1, 38.4]);
        var polyLine = polySeg.join(' ').toString();
        var replacedString = polyLine.replace(/L/g, '').replace(/M/g, "");
        var poly = graph.polygon(replacedString);

        var clip = graph.rect(-80, 0, 80, 40);
        poly.attr({
            'id': 'poly-' + id,
            /*'clipPath':'url(#clip)'*/
                'clipPath': clip
        });
        clip.animate({
            transform: 't80,0'
        }, 1300, mina.linear);
    }
      parseData(points);

      createSegments(myPoints);

    calculatePercentage(points, container);
    joinLine(segments,id);
      drawPolygon(segments, id);

    /*$('#poly-'+id).attr('class','show');*/


    /* function drawPolygon(segments,id){
      var polySeg = segments;
      polySeg.push([80,40],[0,40]);
      var polyLine = segments.join(' ').toString();
      var replacedString = polyLine.replace(/L/g,'').replace(/M/g,"");
      var poly = graph.polygon(replacedString);
      poly.attr('id','poly-'+id)
    }
    drawPolygon(segments,id);*/

}
function drawCircle(container,id,progress,parent){
    var paper = Snap(container);
    var prog = paper.path("M5,50 A45,45,0 1 1 95,50 A45,45,0 1 1 5,50");
    var lineL = prog.getTotalLength();
    var oneUnit = lineL/100;
    var toOffset = lineL - oneUnit * progress;
    var myID = 'circle-graph-'+id;
    prog.attr({
    'stroke-dashoffset':lineL,
    'stroke-dasharray':lineL,
    'id':myID
  });
  var animTime = 1300/*progress / 100*/

  prog.animate({
    'stroke-dashoffset':toOffset
  },animTime,mina.easein);


    function countCircle(animtime,parent,progress){
        var textContainer = $(parent).find('.circle-percentage');
        var i = 0;
        var time = 1300;
        var intervalTime = Math.abs(time / progress);
        var timerID = setInterval(function () {
      i++;
      textContainer.text(i+"%");
      if (i === progress) clearInterval(timerID);
    }, intervalTime);
    }
    countCircle(animTime,parent,progress);
}

// 첫번째 Line Graph data
var chart_1_y = [
    15, 25, 40, 30, 45, 40, 35, 55, 37, 50, 60, 45,70, 78
];
// 두번쨰 Line Graph data
var chart_2_y = [
    80, 65, 65, 40, 55, 34, 54, 50, 60, 64, 55, 27, 24, 30
];



$(window).on('load',function(){
    drawLineGraph('#chart-1', chart_1_y, '#graph-1-container', 1);
    drawLineGraph('#chart-2', chart_2_y, '#graph-2-container', 2);
    drawCircle('#chart-3',1,77,'#circle-1');
    drawCircle('#chart-4',2,53,'#circle-2');
});
