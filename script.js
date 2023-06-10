$(document).ready(function () {
    $('.slider').bxSlider();
});

let link = document.querySelectorAll('.link')
let targetID
link.forEach(function(e){
    e.addEventListener('click', function(event){
        event.preventDefault()
        targetID = e.getAttribute('href')
        document.querySelector(targetID).scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        })
    })
})

navigator.geolocation.getCurrentPosition(function (position) {
    coords = position.coords;     console.log(coords);  
    let latitude = position.coords.latitude;   
   let longitude = position.coords.longitude;  
      let path = 'https://osm.org/go/0wJdXp0vu+++-' + latitude + '/' + longitude;  
});
