window.onscroll = function() {
    let scrollBot = window.pageYOffset;

    if (scrollBot > 200 && scrollBot < 1200) {
        document.querySelector('body').style.backgroundColor = 'rgb(65, 233, 236)';
        document.querySelector('footer').style.backgroundColor = '#15172b';
        document.querySelector('path').fill = '#15172b';
        document.querySelector('.form-container').style.opacity = '1';

    } else {
        document.querySelector('body').style.backgroundColor = 'white';
    }
};



// const btnSub = document.querySelector('.submit');

// btnSub.onclick = () => {
//     window.open("../../templates/account/register_done.html")
// }