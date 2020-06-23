'use strict';


// --- PRELOADER.
function onReady(callback) {
    let intervalId = window.setInterval(function() {
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


function inputsPreparation() {
    document.querySelectorAll('.input').forEach(function(element) {
        element.value = '';
    })

    document.getElementById('input1').focus();
}


setVisibleLevel(false);


onReady(function() {
    inputsPreparation();
    runPreloader(true);
    runPreloader(false);
    setVisibleLevel(true);
});


// --- APPEREANCE OF HIDDEN SOCIAL BUTTONS.
let moreBtn = document.getElementById('more');


moreBtn.addEventListener('click', function() {
    moreBtn.style.display = 'none';
    
    let socialIcons = document.getElementById('socialIcons');
    for (var i = 4; i < socialIcons.children.length; i++) {
        socialIcons.children[i].style.display = 'block';
    }
})



// --- MOVING INPUT'S LABELS.
document.querySelectorAll('.input').forEach(item => {
    item.addEventListener('blur', event => {
        let label = item.nextElementSibling;
        
    if (item.value) {
        label.style.transform = 'translate(-23px, -1px) scale(.85)';
    } else {
        label.style.transform = '';
        label.style.transform = 'translateY(25px); scale(1)';
    }
    })
  })
