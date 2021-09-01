import React, { useEffect, useState } from "react";
import "./App.css";
import { SurahNames } from "./components/SurahNames";

function App() {
	const [surahNames, setSurahNames] = useState([]);

	useEffect(() => {
		fetch("/surah_names").then((response) =>
			response.json().then((data) => {
				setSurahNames(data.surahs);
			})
		);
	}, []);

	return (
		<div className="App">
			<SurahNames surahNames={surahNames} />
		</div>
	);
}

export default App;
