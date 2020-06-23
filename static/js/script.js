'use strict';


// Preloader.
// let authContainer = document.querySelector('.yandex-auth__container');
// authContainer.style.opacity = 0.65;
let loader = document.querySelector('.loader');
let lowVisibleElems = document.querySelectorAll('#low-visible');


function setVisibleLevel(visible) {
    lowVisibleElems.forEach(function(element) {
        // element.style.opacity = 0.33;
        element.style.opacity = visible ? 1 : .45;
    })
}


function onReady(callback) {
    var intervalId = window.setInterval(function() {
      if (document.getElementsByTagName('body')[0] !== undefined) {
        window.clearInterval(intervalId);
        callback.call(this);
      }
    }, 1000);
  }



function runPreloader(visible) {
    // setVisibleLevel(visible);
    // authContainer.style.opacity =  visible ? 0.65 : 1;
    // authContainer.style.opacity =  1;
    loader.style.display = visible ? 'block' : 'none';
}


setVisibleLevel(false);


  
onReady(function() {
    runPreloader(true);
    runPreloader(false);
    setVisibleLevel(true);
});



// Appearing of hidden social buttons.
let moreBtn = document.getElementById('more');
let socialIcons = document.getElementById('socialIcons');


moreBtn.addEventListener('click', function() {
    moreBtn.style.display = 'none';

    for (var i = 4; i < socialIcons.children.length; i++) {
        socialIcons.children[i].style.display = 'block';
    }
})
