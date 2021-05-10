function orderPageMain(){
    pageObj.renderCurrentPage()
    addOrderEventListeners()
}


function makeFormObject() {
    return {
        name: document.getElementById('order-form-name').value,
        street_name: document.getElementById('order-form-street_name').value,
        house_number: document.getElementById('order-form-house_number').value,
        city: document.getElementById('order-form-city').value,
        postal_code: document.getElementById('order-form-postal_code').value,
        country: document.getElementById('id_country').value,
        name_of_cardholder: document.getElementById('order-form-name_of_cardholder').value,
        card_number: document.getElementById('order-form-card_number').value,
        expiration_year: document.getElementById('order-form-expiration_year').value,
        expiration_month: document.getElementById('order-form-expiration_month').value,
        cvc: document.getElementById('order-form-cvc').value
    }
}

function insertSummary(obj) {
    document.getElementById('name-readonly').value = obj.name;
    document.getElementById('streetName-readonly').value = obj.street_name;
    document.getElementById('houseNr-readonly').value = obj.house_number;
    document.getElementById('city-readonly').value = obj.city;
    document.getElementById('country-readonly').value = obj.country;
    document.getElementById('postal-readonly').value = obj.postal_code;
    document.getElementById('carholderName-readonly').value = obj.name_of_cardholder;
    document.getElementById('cardNr-readonly').value = obj.card_number;
    document.getElementById('expDate-readonly').value = obj.expiration_month + '/' + obj.expiration_year;
    document.getElementById('cvc-readonly').value = obj.cvc;

}




const pageState = {
    page: 1,
    nextPage: function(){ if (this.page !== 3) {
        this.page++;
        pageObj.renderCurrentPage();
    }},
    prevPage: function(){ if (this.page !== 1) {
        this.page--;
        pageObj.renderCurrentPage();
    }}
};


const pageObj = {
    pageOne: document.getElementById('page-1'),
    pageTwo: document.getElementById('page-2'),
    pageThree: document.getElementById('page-3'),
    hideAllPages: function() {
        this.pageOne.style.display = 'None';
        this.pageTwo.style.display = 'None';
        this.pageThree.style.display = 'None';
    },
    renderCurrentPage: function() {
        this.hideAllPages();
        if (pageState.page === 1){
            this.pageOne.style.display = 'block'
        } else if (pageState.page === 2) {
            this.pageTwo.style.display = 'block'
        } else if (pageState.page === 3) {
            let obj = makeFormObject();
            this.pageThree.style.display = 'block'
            insertSummary(obj)
        }
    }
}


function addOrderEventListeners(){
    const nextButtons = document.querySelectorAll('#order-next-button');
    const prevButtons = document.querySelectorAll('#order-prev-button');

    for(let i=0; i < nextButtons.length; i++) {
        let btn = nextButtons[i];
        btn.addEventListener('click', e => {
            pageState.nextPage()
        })
    };
    for(let i=0; i < prevButtons.length; i++) {
        let btn = prevButtons[i];
        btn.addEventListener('click', e => {
            pageState.prevPage();
        })
    }
}





orderPageMain()


