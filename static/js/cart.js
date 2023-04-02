var updateBtns = document.getElementsByClassName('update-cart')

for(i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId',productId,'action',action)
        console.log("User", user)

        if(user==="AnonymousUser"){
            console.log("User Not Logged in")
        }else{
            updateUserOrder(productId,action)
        }
    })
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
        location.reload();
    })
}   