document.addEventListener('DOMContentLoaded', function () {
    const teeth = document.querySelectorAll('.tooth');

    teeth.forEach(tooth => {
        tooth.addEventListener('click', function () {
            this.classList.toggle('active');
        });
    });
});