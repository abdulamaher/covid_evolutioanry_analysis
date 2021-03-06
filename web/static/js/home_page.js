var selectedIcons = []
var selectedVariants = null

function iconClickHandler(e) {

	// Keep track of two most recent icons clicked

	if (selectedIcons.includes(e.id)) {
		// Already selected icon clicked, remove it
		selectedIcons.splice(selectedIcons.indexOf(e.id), 1);
		e.style.opacity = 0.5;
	} else {
		// Delete previously selected icons
		while (selectedIcons.length >= 2) {
			selectedIcons.shift();
		}
		// Add the clicked icon
		selectedIcons.push(e.id);
		e.style.opacity = 1;
	}

	console.log(selectedIcons);

}


function getResultClickHandler(e) {
	if (selectedIcons.length != 2) {
		alert("You need to select two animals for comparison!");
	} else if (selectedVariants == null) {
		alert("You need to select a coronavirus variant!")
	} else {
		animal1 = selectedIcons.sort()[0];
		animal2 = selectedIcons.sort()[1];
		window.location = "/results/" + animal1 + '/' + animal2;
	}
}

function variantClickHandler(e) {
	selectedVariants = selectedVariants == e.id ? null : e.id;
	if (selectedVariants == e.id) {
		e.style.opacity = 1;
	} else {
		e.style.opacity = 0.5;
	}
}