async function updateNav() {
    const counter = document.querySelector('#cart-counter-display');
    const count = await getCount();
    counter.innerHTML = count;
}


async function getCount() {
    const res = await axios.get('/cart/get_item_count/')
    return res.data.data;
}


window.onload = e => {
    updateNav();
}




