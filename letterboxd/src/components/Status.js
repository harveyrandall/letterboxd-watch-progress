import React from 'react';

const Status = ({dayOfYear, progress, watched}) => {
    return (
        <div className="status-row">
            <Box message="Day of the year" value={dayOfYear} />
            <Box message="Total films watched" value={watched} />
            <ProgressBox progress={progress} />
        </div>
    );
}

const Box = (props) => {
    let boxClass = props.cssClass ? `status-box ${props.cssClass}` : "status-box";
    return (
        <div className={boxClass}>
            <p>{props.message}</p>
            <h2>{props.value}</h2>
        </div>
    )
}

const ProgressBox = ({progress}) => {
    let message = "Days behind";
    let cssClass = "positive";
    if(progress > 0) {
        message = "Days ahead";
    } else if (progress < 0) {
        cssClass = "negative";
    } 
    return (
        <Box message={message} value={Math.abs(progress)} cssClass={cssClass} />
    )
}

export default Status;