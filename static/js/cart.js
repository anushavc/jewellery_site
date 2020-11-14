var updateBtns=document.getElementsByClassName('update-cart')
console.log('jj')
for(var i=0;i< updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productid=this.dataset.product
        var action=this.dataset.action
        console.log('productId',productid,'action:',action)
    })

}
console.log('user',user)
if(user=='AnonymousUser')
{
    console.log('user not authenticated')
}
else
{
    updateUserOrder(productid,action)
}


function updateUserOrder(productid,action)
{
    console.log('user is logged in,sending data..')

    var url='/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringfy({'productid':productid,'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
    console.log('data:',data)
    location.reload()
})
}