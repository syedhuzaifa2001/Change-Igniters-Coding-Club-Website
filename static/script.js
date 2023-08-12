// navbar
let subMenu = document.getElementById("subMenu");
function toggleMenu() {
  subMenu.classList.toggle("open-menu");

  document.addEventListener("click", function (event) {
    if (
      event.target.closest(".user-pic") === null &&
      event.target.closest(".sub-menu-wrap") === null
    ) {
      subMenu.classList.remove("open-menu");
    }
  });
}

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


