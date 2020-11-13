var updateBtns=document.getElementsByClassName('update-cart')
console.log('jj')
for(var i=0;i< updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productid=this.dataset.product
        var action=this.dataset.action
        console.log('productId',productid,'action:',action)
    })

}