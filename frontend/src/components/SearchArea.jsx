import React, { useState } from "react"
import { tamil_unicode_utf8_replace } from "../tamil"
import axios from "axios"
import Result from "./Result"

const SearchArea = () => {
  const [enText, setEnText] = useState("")
  const [taText, setTaText] = useState("")
  const [result, setResult] = useState([])
  const [loading, setLoading] = useState(false)

  const handleSubmit = () => {
    var bodyFormData = new FormData()
    bodyFormData.append("tamil_text", taText)
    bodyFormData.append("english_text", enText)
    setLoading(true)
    axios({
      method: "post",
      url: "http://127.0.0.1:5000",
      data: bodyFormData,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then((res) => {
        console.log(res)
        setResult(res.data.hits.hits)
        setLoading(false)
      })
      .catch((err) => console.error(err))
  }

  return (
    <div className="search-result-container">
      <div className="search-area">
        <div className="input-container">
          <input
            type="text"
            placeholder="English"
            onChange={(e) => {
              setEnText(e.target.value)
              console.log(enText)
            }}
          />
          <input
            type="text"
            placeholder="Romanized Tamil"
            onChange={(e) => {
              setTaText(
                tamil_unicode_utf8_replace(e.target.value.toLowerCase())
              )
              console.log(taText)
            }}
          />
        </div>
        <p>{(enText + " " + taText).trim()}</p>
        <button onClick={handleSubmit}>SEARCH</button>
      </div>
      <div className="result-area">
        {result.map((result) => (
          <Result score={result._score} title={result._source.title} />
        ))}
      </div>
    </div>
  )
}

export default SearchArea
