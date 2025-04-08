let RunSentimentAnalysis = () => {
	textToAnalyze = document.getElementById('textToAnalyze').value
	console.log(textToAnalyze)

	let xhttp = new XMLHttpRequest()
	xhttp.onreadystatechange = function () {
		document.getElementById('system_response').innerHTML =
			xhttp.responseText
	}
	xhttp.open('POST', 'http://127.0.0.1:5000/emotionDetector', true)
	xhttp.setRequestHeader('Content-Type', 'application/json')
	xhttp.send(JSON.stringify({ text: textToAnalyze }))
	xhttp.send()
}
