window.onload = (event) => {
  test();
};


async function test() {
    const res = await axios({
        method: "get",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
            "content-type": "application/json"
        },
        url: '/get_product_data/'
    });

    console.log(res)
}



function renderItems(itemArray){

}
