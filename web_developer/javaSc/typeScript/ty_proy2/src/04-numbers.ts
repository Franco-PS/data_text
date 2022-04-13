(()=>{
  let productPrice = 100;
  productPrice = 12;
  console.log('productPrice', productPrice);

  let customerAge: number = 28;
  customerAge= customerAge + '1';

  let productInStock: number;    //cuando no se asigna la variable se debe de poner el tipo de dato explicito
  console.log(productInStock);

  if(productInStock > 10){
    console.log('tienes un stock mayor a 10');
  }

  let discount = parseInt('las');
  console.log('discount', discount);
})();
