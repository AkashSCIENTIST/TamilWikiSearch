import React, { useState, useRef, useEffect } from "react";
import { tamil_unicode_utf8_replace } from "../tamil";
import axios from "axios";
import Result from "./Result";
import logo from "/logo.svg";
import search from "/search.svg";
import book from "/book.gif";

const SearchArea = () => {
  const [enText, setEnText] = useState("");
  const [taText, setTaText] = useState("");
  const [result, setResult] = useState([]);
  const [loading, setLoading] = useState(false);
  const [firstTime, setFirstTime] = useState(true);

  const firstInput = useRef();

  const handleSubmit = (e) => {
    e.preventDefault();
    var bodyFormData = new FormData();
    bodyFormData.append("tamil_text", taText);
    bodyFormData.append("english_text", enText);
    setLoading(true);
    axios({
      method: "post",
      url: "http://127.0.0.1:5000",
      data: bodyFormData,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then((res) => {
        console.log(res);
        setFirstTime(false);
        setResult(res.data.hits.hits);
        setLoading(false);
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="search-result-container">
      <div className="header">
        <img src={logo} alt="" className="logo" />
        <form className="input-container">
          <input
            type="text"
            placeholder="Romanized Tamil"
            className="input-fields"
            onChange={(e) => {
              setTaText(
                tamil_unicode_utf8_replace(e.target.value.toLowerCase())
              );
              console.log(taText);
            }}
          />
          <input
            type="text"
            placeholder="English"
            className="input-fields"
            ref={firstInput}
            onChange={(e) => {
              setEnText(e.target.value);
              console.log(enText);
            }}
          />
          <input
            type="text"
            placeholder="Result"
            className="input-fields"
            ref={firstInput}
            disabled
            value={(enText + " " + taText).trim()}
          />

          <button
            type="submit"
            onClick={handleSubmit}
            className="submitBtn"
          ></button>
        </form>
        {/* <p>{(enText + " " + taText).trim()}</p> */}
      </div>

      {firstTime ? (
        <img src={book} alt="" className="first-time-gif" />
      ) : (
        <div className="result-area">
          {result.map((result) => (
            <Result score={result._score} title={result._source.title} />
          ))}
        </div>
      )}
    </div>
  );
};

export default SearchArea;
