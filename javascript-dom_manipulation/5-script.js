const updateHeaderTrigger = document.querySelector('#update_header');
const header = document.querySelector('header');

updateHeaderTrigger.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
