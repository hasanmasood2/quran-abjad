import React from "react";
import Table from "react-bootstrap/Table";

export const SurahNames = ({ surahNames }) => {
	return (
		<Table responsive striped bordered hover>
			<thead>
				<tr>
					<th>#</th>
					<th>Surah Name</th>
					<th>Number of Verses</th>
					<th>Surah Name Abjad Value</th>
				</tr>
			</thead>
			<tbody>
				{surahNames.map((element, index) => (
					<tr key={index}>
						<td>{element.surah_number}</td>
						<td>{element.surah_name}</td>
						<td>{element.number_of_verses}</td>
						<td>{element.abjad_score}</td>
					</tr>
				))}
			</tbody>
		</Table>
	);
};
