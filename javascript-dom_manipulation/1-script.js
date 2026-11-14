const redHeaderTrigger = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeaderTrigger.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
