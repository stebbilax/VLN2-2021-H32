





function addEventListeners() {
    const incrementButtons = document.querySelectorAll(".increment-button");
    const decrementButtons = document.querySelectorAll(".decrement-button");

    incrementButtons.forEach(btn => btn.addEventListener('click', e => {
        try{
            increment(e.target.getAttribute('name'));
        } catch (error) {
            console.error(error);
        }
    }));

    decrementButtons.forEach(btn => btn.addEventListener('click', e => {
        try{
            decrement(e.target.getAttribute('name'));
        } catch (error) {
            console.error(error);
        }
    }));
}

// Requests incrementing quantity on the backend
async function increment(itemId){
    const res = await axios({
        method: "post",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
            "content-type": "application/json"
        },
        url: '/cart/increase_quantity/' + itemId.toString()
    });
    if(res.status == 200){

        const quantity = res.data;
        updateQuantity(itemId, quantity);
    }
}


// Requests decrementing quantity on the backend
async function decrement(itemId){
    const res = await axios({
        method: "post",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
            "content-type": "application/json"
        },
        url: '/cart/decrease_quantity/' + itemId.toString()
    });
    if(res.status == 200){
        const quantity = res.data;
        updateQuantity(itemId, quantity);
    }
}


// Updates quantity if not 0. Removes element if quantity is 0
function updateQuantity(itemId, quantity){
    const item = document.querySelector(`#item-${itemId}`);
    const card = document.querySelector(`#card-${itemId}`);
    if (item){
        if(quantity === 0){
            card.remove();
        } else {
            item.innerHTML = quantity;
        }
    }
    getSummaryInfo();
}


async function getSummaryInfo(){
    const res = await axios({
        method: "post",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
            "content-type": "application/json"
        },
        url: '/cart/get_summary_info/'
    });
    console.log(res.data)
    document.getElementById('summary-total').innerHTML = '$' + res.data.summary.total;
}


addEventListeners();



