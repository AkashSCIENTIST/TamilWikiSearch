import React from "react";

const Result = ({ score, title }) => {
  const redirect = () => {
    window.open("https://tamil.wiki/wiki/" + title, "_blank");
  };
  return (
    <div className="result" onClick={redirect}>
      <h2>{title}</h2>
      <br />
      <p>{score}</p>
    </div>
  );
};

export default Result;
