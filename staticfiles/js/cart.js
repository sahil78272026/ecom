var updateBtns = document.getElementsByClassName('update-cart')

for(i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId',productId,'action',action)
        console.log("User", user)

        if(user=="AnonymousUser"){
            addCookieItem(productId,action)
        }else{
            updateUserOrder(productId,action)
        }
    })
}

function addCookieItem(productId,action){
    console.log("Not Logged In...")

    if(action=='add'){
        console.log('Action: ', action)

        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
            console.log('Undefined cart[productId]: ', cart[productId])
        }else{
            console.log('updatedcart[productId]: ', cart[productId])
            cart[productId]['quantity']+=1
        }
    }  

    if(action=='remove'){
        cart[productId]['quantity']-=1

        if(cart[productId]['quantity']<=0){
            console.log("Item Removed")
            delete cart[productId]
        }
    }

    document.cookie = 'cart='+JSON.stringify(cart)+";domain=;path=/"
    console.log('Cart: ', cart)
    // location.reload()
}

function updateUserOrder(productId,action){
    console.log("User is logged IN, Sending Data....")
    var url = '/update_item/' // django backend url

    // using fetch api, posting data and getting data from backend
    // only url is mandatory, rest is optional, if not given, default request would be 'GET'
    // django doesn't allow request to backend without csrf token
    // csrf token for post data from fetch API
    // see getCookie(name) in main.html for csrf token
    fetch(url,{
        method:'POST', // method type
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken': csrftoken 
            
     },
     body:JSON.stringify({'productId':productId,'action':action}) // sending data in body in string format

    })


    // fetch api return a promise
    .then((response) => {
        return response.json()
        
    })
    .then((data)=>{
        console.log('data', data)
    
    })
}   