window.onload = (event) => {
  main();
};

// Keeps track of all query parameters currently in use
const queryParameters = {
    price: '',
    keyword:'',
    order:'',
    category:'',
    setPrice: function(price){ this.price = price },
    setKeyword: function(keyword){ this.keyword = keyword},
    setOrder: function(order){ this.order = order},
    setCategory: function(category){ this.category = category},
    getQueryString: function() {
        let str = '?';
        if(this.price !== '') {str += 'price='+this.price.toString()+'&'}
        if(this.keyword !== '') {str += 'keyword='+this.keyword.toString()+'&'}
        if(this.order !== '') {str += 'order='+this.order.toString()+'&'}
        return str;
    }
}


async function makeRequest() {
    const res = await axios({
        method: "get",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
            "content-type": "application/json"
        },
        url: '/get_product_data/' + queryParameters.category + '/' + queryParameters.getQueryString()
    });
    return res.data.products;
}


function addListeners() {
    // Order buttons
    const orderByButtons = document.querySelectorAll('.order-by-button');
    for(let i=0; i < orderByButtons.length; i++) {
        let button = orderByButtons[i];
        button.addEventListener('click', e => {
            queryParameters.setOrder(e.target.name);
            refresh();
        })
    };

    // Price buttons
    const priceByButtons = document.querySelectorAll('.price-by-button');
    for(let i=0; i < priceByButtons.length; i++) {
        let button = priceByButtons[i];
        button.addEventListener('click', e => {
            queryParameters.setPrice(e.target.name);
            refresh();
        })
    };

    // Keyword buttons
    const keywordByButtons = document.querySelectorAll('.keyword-by-button');
    for(let i=0; i < keywordByButtons.length; i++) {
        let button = keywordByButtons[i];
        button.addEventListener('click', e => {
            queryParameters.setKeyword(e.target.name);
            refresh();
        })
    }
}



function renderItems(itemArray){
    const container = document.querySelector('#product-card-container');
    const parser = new DOMParser();
    clearItems();
    for(let i=0; i < itemArray.length; i++){
        let product = itemArray[i];
        let text = `
            <div class="col">
                <div class="shadow-sm card h-100 p-3 text-center text-decoration-none">
                    <img src="${product.img}" class="card-img-top mx-auto" alt="..." style="width: auto; max-height: 150px">
                    <div class="card-body">
                    <h5 class="card-title">${product.name }</h5>
                    <p class="card-text">Price: ${product.price}</p>
                    <a href="../product/product.html" class="stretched-link"></a>
                    <a href="../cart/cart.html" class="btn btn-primary">Add to cart</a>
                    </div>
                </div>
            </div>
        `;
        let doc = parser.parseFromString(text, 'text/html');
        container.appendChild(doc.body.firstChild);
    }
};

function clearItems() {
    const cardContainer = document.querySelector('#product-card-container');
    const searchContainer = document.querySelector('#product-search-bar');
    cardContainer.innerHTML = '';
    searchContainer.value = '';
}

async function refresh() {
    let items = await makeRequest();
    renderItems(items);
}


function getAndSetCategory() {
    const category = window.location.pathname.split('/').filter(el => el);
    queryParameters.setCategory(category[1]);
}

async function getKeywords(){
    const res = await axios({
        method: "get",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
            "content-type": "application/json"
        },
        url: '/keywords/'
    });
    return res.data.keywords;
}

function buildKeywordPanel(keywords) {
    const container = document.querySelector('#keyword-container');
    const parser = new DOMParser();
    for(let i=0; i < keywords.length; i++) {
        let keyword = keywords[i];
        let text = `
            <label class="form-check">
                <input class="form-check-input keyword-by-button" name="${keyword}" type="checkbox" value="">
                <span class="form-check-label">${keyword}</span>
            </label>
        `
        let doc = parser.parseFromString(text, 'text/html');
        container.appendChild(doc.body.firstChild);
    }
}



async function main() {
    const keywords = await getKeywords();
    buildKeywordPanel(keywords);

    getAndSetCategory();
    addListeners();
}

