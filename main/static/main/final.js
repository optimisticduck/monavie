let carts = document.querySelectorAll('.add-cart');

let products = 
[
    {
        name: 'Beef',
        tag: 'Beef',
        price: 600,
        inCart:0
    },
    {
        name: 'Mutton',
        tag: 'Mutton',
        price: 900,
        inCart:0
    },
    {
        name: 'Carabeef',
        tag: 'Carabeef',
        price: 400,
        inCart:0
    },
    {
        name: 'Jerky',
        tag: 'Jerky',
        price: 400,
        inCart:0
    },
    {
        name: 'Biltong',
        tag: 'Biltong',
        price: 400,
        inCart:0
    },
    {
        name: 'Salt beef',
        tag: 'Salt beef',
        price: 1200,
        inCart:0
    },
    {
        name: 'Tea',
        tag: 'Tea',
        price: 200,
        inCart:0
    },
    {
        name: 'Spice pack',
        tag: 'Spice pack',
        price: 300,
        inCart:0
    },
    {
        name: 'Paneer',
        tag: 'Paneer',
        price: 700,
        inCart:0
    },
    
]

for(let i=0; i<carts.length;i++)
{
    carts[i].addEventListener('click', () => 
    {
        cartNumbers(products[i]);
        totalCost(products[i]);
    })
}

function onLoadCartNumbers()
{
    let productNumbers = localStorage.getItem('cartNumbers');
    
    if( productNumbers )
    {
        document.querySelector('.cart span').textContent=productNumbers;
    }
}
function cartNumbers(product)
{
    console.log('P c', product)
    let productNumbers = localStorage.getItem('cartNumbers');
    productNumbers = parseInt(productNumbers);
    
    if( productNumbers )
    {
        localStorage.setItem('cartNumbers', productNumbers+1);
        document.querySelector('.cart span').textContent=productNumbers+1;
    }
    else
    {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.cart span').textContent=1;
    }
    setItems(product);
}

function setItems(product){

    let cartItems= localStorage.getItem('productsInCart');  
    cartItems = JSON.parse(cartItems);
    localStorage.setItem("productsInCart", JSON.stringify(cartItems));


    if(cartItems!=null)
    {
        if(cartItems[product.tag] == undefined)
        {
            cartItems=
            {
                ...cartItems,
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart+=1;
    }
    else 
    {
        product.inCart=1;
        cartItems={
            [product.tag]:product
        }
    }  
    
    localStorage.setItem("productsInCart", JSON.stringify(cartItems));
}

function totalCost(product)
{
    //console.log("The product price is", product.price);
    let cartCost = localStorage.getItem('totalCost');
    console.log("My cart cost is", cartCost);
    
    if(cartCost!=null)
    {
        cartCost = parseInt(cartCost);
        localStorage.setItem("totalCost", cartCost+product.price)
    }
    else
    {
        localStorage.setItem("totalCost", product.price);
    }

}


onLoadCartNumbers();
