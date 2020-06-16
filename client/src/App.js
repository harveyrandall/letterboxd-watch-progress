import React, { useState, useEffect } from 'react';
import './App.css';
import Status from './components/Status';
import LineChart from './components/LineChart';

function App() {
  const currentDay = dayOfYear();
  const [dayDiff, setDayDiff] = useState(0);
  const [totalWatched, setTotalWatched] = useState(0);
  const [data, setData] = useState({});

  let reqHeaders = new Headers();
  reqHeaders.append('pragma', 'no-cache');
  reqHeaders.append('cache-control', 'no-cache');

  useEffect(() => {
    fetch('/api/daily', reqHeaders).then(res => res.json()).then(data => {
      setData(data.diary);
      let total = Object.values(data.diary).reduce((a,b) => {
        return Math.max(a,b);
      })
      setTotalWatched(total);
      setDayDiff(total - currentDay);
    });
  }, [currentDay]);

  return (
    <div className="App">
      <Status
        dayOfYear={currentDay}
        progress={dayDiff}
        watched={totalWatched}
      />
      <LineChart data={data} />
    </div>
  );
}

function dayOfYear() {
  var now = new Date();
  var start = new Date(now.getFullYear(), 0, 1);
  var diff = (now - start) + ((start.getTimezoneOffset() - now.getTimezoneOffset()) * 1000 * 60);
  var oneDay = 1000 * 60 * 60 * 24;
  return Math.ceil(diff/oneDay)
}

export default App;
