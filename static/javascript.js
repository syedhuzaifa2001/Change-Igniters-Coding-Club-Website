// navbar
let subMenu;
subMenu = document.getElementById("subMenu");
function toggleMenu() {
	subMenu.classList.toggle("open-menu");
}

// image slider
console.log("i am javascript file")
var swiper = new Swiper(".slide-content", {
	slidesPerView: 3,
	spaceBetween: 25,
	loop: true,
	centerSlide: "true",
	fade: "true",
	grabCursor: "true",
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
		dynamicBullets: true,
	},
	navigation: {
		nextEl: ".swiper-button-next",
		prevEl: ".swiper-button-prev",
	},

	breakpoints: {
		0: {
			slidesPerView: 1,
		},
		520: {
			slidesPerView: 2,
		},
		950: {
			slidesPerView: 3,
		},
	},
});

// leaderboard

const selectElement = document.getElementById("Leaderboard-selector");

selectElement.addEventListener("change", function () {
	const selectedOption = selectElement.options[selectElement.selectedIndex];

	switch (selectedOption.value) {
		case "0":
			handleOption0Click();
			break;
		case "1":
			handleOption1Click();
			break;
		case "2":
			handleOption2Click();
			break;
		case "3":
			handleOption3Click();
			break;
		default:
			break;
	}
});

function handleOption1Click() {
	// Code to execute when the option "HTML CSS JS" is selected
	document.getElementById("box-1").style.display = "block";
	document.getElementById("box-2").style.display = "none";
	document.getElementById("box-3").style.display = "none";
	document.getElementById("intro").style.height = "565px";
	
}

function handleOption2Click() {
	// Code to execute when the option "Data Science" is selected
	document.getElementById("box-1").style.display = "none";
	document.getElementById("box-2").style.display = "block";
	document.getElementById("box-3").style.display = "none";
	document.getElementById("intro").style.height = "565px";
}

function handleOption3Click() {
	// Code to execute when the option "AI Project" is selected
	document.getElementById("box-1").style.display = "none";
	document.getElementById("box-2").style.display = "none";
	document.getElementById("box-3").style.display = "block";
	document.getElementById("intro").style.height = "565px";
}
function handleOption0Click() {
	// Code to execute when the option "..." is selected
	document.getElementById("box-1").style.display = "block";
	document.getElementById("box-2").style.display = "block";
	document.getElementById("box-3").style.display = "block";
	document.getElementById("intro").style.height = "1200px";
}

// events

// buttons
// event_nav = document.getElementById("event-nav");
// live_btn = event_nav.children[0];
// upcoming_btn = event_nav.children[1];
// previous_btn = event_nav.children[2];

// live_btn.onclick = () => {
// 	live_btn.classList.add("active");
// 	upcoming_btn.classList.remove("active");
// 	previous_btn.classList.remove("active");
// };
// upcoming_btn.onclick = () => {
// 	upcoming_btn.classList.add("active");
// 	live_btn.classList.remove("active");
// 	previous_btn.classList.remove("active");
// };
// previous_btn.onclick = () => {
// 	previous_btn.classList.add("active");
// 	upcoming_btn.classList.remove("active");
// 	live_btn.classList.remove("active");
// };



/*Interactivity to determine when an animated element in in view. In view elements trigger our animation*/

$(document).ready(function () {
	//window and animation items
	var animation_elements = $.find(".animation-element");
	var web_window = $(window);

	//check to see if any animation containers are currently in view
	function check_if_in_view() {
		//get current window information
		var window_height = web_window.height();
		var window_top_position = web_window.scrollTop();
		var window_bottom_position = window_top_position + window_height;

		//iterate through elements to see if its in view
		$.each(animation_elements, function () {
			//get the element sinformation
			var element = $(this);
			var element_height = $(element).outerHeight();
			var element_top_position = $(element).offset().top;
			var element_bottom_position = element_top_position + element_height;

			//check to see if this current container is visible (its viewable if it exists between the viewable space of the viewport)
			if (
				element_bottom_position >= window_top_position &&
				element_top_position <= window_bottom_position
			) {
				element.addClass("in-view");
			} else {
				element.removeClass("in-view");
			}
		});
	}

	//on or scroll, detect elements in view
	$(window).on("scroll resize", function () {
		check_if_in_view();
	});
	//trigger our scroll event on initial load
	$(window).trigger("scroll");
});

// Registration Section
function show1() {
	document.getElementById("div1").style.display = "none";
	document.getElementById("form3Example1T").required = false;
	document.getElementById("form3Example1L").required = false;
}

function show2() {
	document.getElementById("div1").style.display = "block";
	document.getElementById("form3Example1T").required = true;
	document.getElementById("form3Example1L").required = true;
}

$(document).ready(function () {
	$("#multiselect").multiselect({
		buttonWidth: "160px",
		includeSelectAllOption: true,
		nonSelectedText: "Select an Option",
	});
});

function getSelectedValues() {
	var selectedVal = $("#multiselect").val();
	for (var i = 0; i < selectedVal.length; i++) {
		function innerFunc(i) {
			setTimeout(function () {
				location.href = selectedVal[i];
			}, i * 2000);
		}
		innerFunc(i);
	}
}

// function togglePasswordVisibilityReg() {
//   var passwordField = document.getElementById("passwordReg");
//   var showPasswordCheckbox = document.getElementById("showPasswordReg");
//   if (showPasswordCheckbox.checked) {
//     passwordField.type = "text";
//   } else {
//     passwordField.type = "password";
//   }
// }
function togglePasswordVisibilityLog() {
	var passwordField = document.getElementById("passwordLog");
	var showPasswordCheckbox = document.getElementById("showPasswordLog");
	if (showPasswordCheckbox.checked) {
		passwordField.type = "text";
	} else {
		passwordField.type = "password";
	}
}

// image slider

// Show the modal when the form is submitted
contModal.classList.add("showCont");

// Hide the modal after 4 seconds
setTimeout(function () {
	contModal.classList.remove("showCont");
}, 3000);
