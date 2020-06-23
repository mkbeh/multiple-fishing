'use strict';


// Preloader.
function onReady(callback) {
    var intervalId = window.setInterval(function() {
      if (document.getElementsByTagName('body')[0] !== undefined) {
        window.clearInterval(intervalId);
        callback.call(this);
      }
    }, 1000);
  }



function runPreloader(visible) {
    document.querySelector('.loader').style.display = visible ? 'block' : 'none';
}


function setVisibleLevel(visible) {
    document.querySelectorAll('#low-visible').forEach(function(element) {
        element.style.opacity = visible ? 1 : .45;
    })
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
