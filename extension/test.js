function setScreenshotUrl(url) {
	document.getElementById("target").src = url;
}

chrome.runtime.onMessage.addListener(function (request) {
	if (request.msg === "screenshot") {
		setScreenshotUrl(request.data);

		console.log(request.data);
		// StartAnimation()

		// fetch("http://127.0.0.1:5000/generate-content", {
		// 	method: "POST",
		// 	headers: {
		// 		"Content-Type": "application/json",
		// 	},
		// 	body: JSON.stringify({ data: request.data }),
		// })
		// 	.then((res) => res.json())
		// 	.then((data) => {
		// 		console.log(data);

		// StopAnimatioon()

		// 	})
		// 	.catch((err) => {
		// 		console.error(err);
		// 	});

		fetch("http://127.0.0.1:5000/ping")
			.then((res) => res.json())
			.then((data) => {
				console.log(data);
			})
			.catch((err) => {
				console.error(err);
			});
	}
});
