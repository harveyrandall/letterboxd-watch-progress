import React, {useEffect, useRef} from 'react';
import Chart from "chart.js";

const LineChart = (props) => {
    const chartRef = useRef(null);
    const labels = Object.keys(props.data);
    const watchedData = Object.values(props.data);
    let avgData = [];
    for(let i=1; i <= labels.length; i++) {
        avgData.push(i);
    }
    const chartConfig = {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Watched",
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: "rgb(255, 99, 132)",
                    fill: false,
                    data: watchedData
                },
                {
                    label: "One a day average",
                    backgroundColor: "rgb(54, 162, 235)",
                    borderColor: "rgb(54, 162, 235)",
                    fill: false,
                    data: avgData
                }
            ]
        },
        options: {
            responsive: true,
            showXLabels: 10,
            title: {
                display: true,
                text: "Progress vs. Average"
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true,
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Day',
                        fontSize: 16
                    },
                    type: 'time',
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 12
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: "Count",
                        fontSize: 16
                    }
                }]
            }
        }
    }

    useEffect(() => {
        if(chartRef.current) {
            const newChart = new Chart(chartRef.current, chartConfig);
        }
    }, [chartRef, chartConfig])

    return (
        <canvas id="watched" ref={chartRef} />
    )
}

export default LineChart;