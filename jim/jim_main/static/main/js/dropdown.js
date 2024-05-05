console.log(document.querySelector('.table-responsive'))


document.querySelectorAll('.dropdown').forEach(element => {
    console.log("hehe")
    dropDownBtn = element.querySelector('.dropdown_button');

    dropDownBtn.addEventListener('click', function () {
        const dropdownlists = element.querySelectorAll('.dropdown_list')
        dropdownlists.forEach(element => {
            element.classList.toggle('dropdownListVisible');
        });
    });


});

