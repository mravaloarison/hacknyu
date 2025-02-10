document.addEventListener("DOMContentLoaded", () => {
	const c1 = document.getElementById("percentage-text-1");
	const c2 = document.getElementById("percentage-text-2");
	const c3 = document.getElementById("percentage-text-3");

	const c1_text = document.getElementById("c1-text");
	const c2_text = document.getElementById("c2-text");
	const c3_text = document.getElementById("c3-text");

	const toggleBtns = document.querySelectorAll("button.acc");

	const toggle_ai = document.getElementById("toggle-ai");
	const toggle_harmful = document.getElementById("toggle-harmful");
	const toggle_scam = document.getElementById("toggle-scam");

	const c1_section = document.getElementById("c1-details");
	const c2_section = document.getElementById("c2-details");
	const c3_section = document.getElementById("c3-details");

	// ACCORDION
	function toggleAccordion(button) {
		const content = button.nextElementSibling;
		const icon = button.querySelector(".icon");

		try {
			if (content.classList.contains("hidden")) {
				content.classList.remove("hidden");
				content.style.maxHeight = content.scrollHeight + "px";
				icon.style.transform = "rotate(90deg)";
			} else {
				content.style.maxHeight = "0px";
				setTimeout(() => content.classList.add("hidden"), 300);
				icon.style.transform = "rotate(0deg)";
			}
		} catch {
			console.log("Error toggling accordion.");
		}
	}

	const accordionButtons = document.querySelectorAll("button.acc");
	accordionButtons.forEach((button) => {
		button.addEventListener("click", () => toggleAccordion(button));
	});

	// ANIMATIION CIRCLES
	function updateProgressCircle(circleId, textId, percentage, colorClass) {
		const circle = document.getElementById(circleId);
		const text = document.getElementById(textId);

		let color;
		switch (colorClass) {
			case "circle-blue":
				color = " #36A2EB";
				break;
			case "circle-green":
				color = " #FFCE56";
				break;
			case "circle-red":
				color = " #FF6384";
				break;
			default:
				color = "#D1D5DB";
		}

		circle.style.stroke = color;

		text.style.color = color;

		const offset = 100 - percentage;

		circle.classList.add("progress-circle");

		circle.style.strokeDashoffset = offset;

		text.textContent = `${percentage}%`;
	}

	function resetCircles() {
		const circles = document.querySelectorAll("circle");
		const percentageTexts = document.querySelectorAll(
			"span.circles_percentage"
		);

		c1_section.innerHTML = `<p class="p-3 text-gray-700">Nothing to show</p>`;
		c2_section.innerHTML = `<p class="p-3 text-gray-700">Nothing to show</p>`;
		c3_section.innerHTML = `<p class="p-3 text-gray-700">Nothing to show</p>`;

		circles.forEach((circle) => {
			circle.classList.remove("progress-circle");
			circle.style.stroke = "#D1D5DB";
			circle.style.strokeDashoffset = 100;
		});
		percentageTexts.forEach((span) => {
			span.textContent = "0%";
			span.style.color = "#D1D5DB";
		});
		toggleBtns.forEach((btn) => {
			if (!btn.classList.contains("text-gray-400")) {
				btn.classList.add("text-gray-400");
			}

			btn.classList.forEach((cls) => {
				if (cls.startsWith("text-[")) {
					btn.classList.remove(cls);
				}
			});
		});
	}

	// LOADING
	const startBtn = document.getElementById("startBtn");
	const diagnosticBtn = document.getElementById("diagnosticBtn");
	let isRunning = false;

	startBtn.addEventListener("click", async () => {
		startDiagnostics();
		resetCircles();

		const screenshotUrl = await chrome.tabs.captureVisibleTab();
		fetch("http://127.0.0.1:5000/generate-content", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ data: screenshotUrl }),
		})
			.then((res) => res.json())
			.then((data) => {
				console.log(data);

				stopDiagnostics();

				const percentages = {
					circle1: data.ai_generated.confidence * 100,
					circle2: data.harmful_content.confidence * 100,
					circle3: data.scam_likelihood.confidence * 100,
				};

				c1.innerHTML = data.ai_generated.confidence * 100;
				c2.innerHTML = data.harmful_content.confidence * 100;
				c3.innerHTML = data.scam_likelihood.confidence * 100;

				c1_text.innerHTML = data.ai_generated.confidence * 100 + "%";
				c2_text.innerHTML = data.harmful_content.confidence * 100 + "%";
				c3_text.innerHTML = data.scam_likelihood.confidence * 100 + "%";

				toggleBtns.forEach((btn) => {
					if (btn.classList.contains("text-gray-400")) {
						btn.classList.remove("text-gray-400");
					}
				});

				toggle_ai.classList.add("text-[#36A2EB]");
				toggle_harmful.classList.add("text-[#FFCE56]");
				toggle_scam.classList.add("text-[#FF6384]");

				c1_text.classList.add("text-[#36A2EB]");
				c2_text.classList.add("text-[#FFCE56]");
				c3_text.classList.add("text-[#FF6384]");

				if (
					data.ai_generated.reasons.length > 0 ||
					data.ai_generated.where_in_content.length > 0
				) {
					c1_section.innerHTML = createTable(data.ai_generated);
				}

				if (
					data.harmful_content.reasons.length > 0 ||
					data.harmful_content.where_in_content.length > 0
				) {
					c2_section.innerHTML = createTable(data.harmful_content);
				}

				if (
					data.scam_likelihood.reasons.length > 0 ||
					data.scam_likelihood.where_in_content.length > 0
				) {
					c3_section.innerHTML = createTable(data.scam_likelihood);
				}

				updateProgressCircle(
					"progress-circle-1",
					"percentage-text-1",
					percentages.circle1,
					"circle-blue"
				);
				updateProgressCircle(
					"progress-circle-2",
					"percentage-text-2",
					percentages.circle2,
					"circle-green"
				);
				updateProgressCircle(
					"progress-circle-3",
					"percentage-text-3",
					percentages.circle3,
					"circle-red"
				);
			})
			.catch((err) => {
				console.error(err);
			});
	});

	function startDiagnostics() {
		if (isRunning) return;
		isRunning = true;
		startBtn.classList.add("hidden");
		diagnosticBtn.classList.remove("hidden");
	}

	function stopDiagnostics() {
		if (!isRunning) return;
		isRunning = false;

		diagnosticBtn.classList.add("hidden");
		startBtn.classList.remove("hidden");

		console.log("Diagnostics stopped.");
	}

	function createTable(data) {
		return `
            <table class="table-auto border-collapse border border-gray-400 w-full">
                <thead>
                    <tr>
                        <th></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="border border-gray-400 border-t-0 p-2 font-semibold">Reasons</td>
                        <td class="border border-gray-400 border-t-0 w-full p-2">
                            <div class="px-4">
                                <ul class="list-disc">
                                    ${data.reasons
										.map((reason) => `<li>${reason}</li>`)
										.join("")}
                                </ul>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td class="border border-gray-400 p-2 font-semibold">Where</td>
                        <td class="border border-gray-400 w-fll p-2">
                            <div class="px-4">
                                <ul class="list-disc">
                                    ${data.where_in_content
										.map((where) => `<li>${where}</li>`)
										.join("")}
                                </ul>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        `;
	}

	// Function to update the content of a section
	function updateSection(sectionId, data) {
		const section = document.getElementById(sectionId);
		section.innerHTML = "";

		if (data.reasons.length > 0 || data.where_in_content.length > 0) {
			section.innerHTML = createTable(data); // Replace with table if data exists
		} else {
			section.innerHTML = `<p class="p-3 text-gray-700">Nothing to show</p>`; // Keep default message if no data
		}
	}
});
