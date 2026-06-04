// const readline = require("readline");

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question("Misol kiriting (masalan 5+3): ", (input) => {

//     try {
//         const result = eval(input);
//         console.log("Natija:", result);
//     } catch {
//         console.log("Xatolik!");
//     }

//     rl.close();
// });




// let x=9;
// let y=x++ + ++x;
// console.log("x:%d",x);
// console.log("y:%d",y);

// let a=3,b=6,c=12;
// if(a<b)a=b;
// if(a<c)a=c;
// console.log(a);

// let a=3,b=5,c=7;
// a=(a>b)?a:b;
// a=(a>c)?a:c;
// console.log(a);


// let x=5;
// if(x>0){
//     console.log("Musbat");
// }else if(x<0){
//     console.log("Manfiy");
// }else{
//     console.log("Nol");
// }


// let x=3
// let s=(x>0)?"Musbat":
//     (x<0)?"Manfiy":"Noll";
// console.log(s)


// let x=3
// switch(x){
//     case 1:
//         console.log("Bahor");break;
//     case 2:
//         console.log("Yoz");break;
//     case 3:
//         console.log("Kuz");break;
//     case 4:
//         console.log("Qish");break;
//     default:
//         console.log("1 dan 4 gacha son kirit")
// }
 // for(let i=0;i<10;i++){
//     if(i ===5){
//         break;
//     }
//     console.log
// }


// let i=1;
// do{
//     if (i===5){
//         console.log(i);
//     }i++;
//     break;
//     }while (i <=10);



// rl.question('finish:',(input))=>{
//     input=parseInt(input);
//     for (let i=0; i<1000;i++){
//         if(i % input ===0)
//     }
// }




// let k =[2,3,4,5,6,7,8,9];
// let x=-4
// let tekshir=false;
// for(let i=0;i<k.length;i++){
//     if(k[i]===x){
//         tekshir=true;
//         break;
//     }
// }
// let result=tekshir? ${x}-soni bor:${x}-soni yoq;
// console.log(result);


// let n=['toyota','mazda','chevrolet','honda','suzuki'];
// let result = n.find(item => item.endsWith('da'));
// console.log(result);
// for (let i=1;i<=4;i++){
//     console.log(${i}-hafta);
//     for (let j=1;j<=7;j++){
//         console.log(${j}-kun);
//     }
// }


// let i=1;
// do{
//     console.log(${i}-hafta);
//     let j=1;
//     while(j<=7){
//         console.log(/t${j}-kun);
//         j++;
//     }
//     i++
// }while(i<=4)



// let k =[1,23,34,67,-98,7];
// let count=0;
// for (let x of k){
//     x=Math.abs(x);
//     while(x>0){
//         count++;
//         x=Math.floor(x/10);
//     }
// }
// console.log(${k}=>raqamlar soni ${count});



// let k=[1,23,34,67,-98,7,-12];
// let x=k.join('').toString();
// let count =0;
// for(let y of x){
//     if (y !==''&& y !=='-'){
//         count++;
//     }
// }
// console.log(count)


// let x=32;
// let tubmi =true;
// for(let i=2;i<= Math.sqrt(x); i++){
//     if (x % i ===0){
//         tubmi=false;
//         break;
//     }
// }
// if(tubmi){
// console.log("Tub son");
// }else{
//     console.log("Tub son esam")
// }



// let k = ['toyota','mazda','chevrolet','honda','suzuki','audi'];

// for(let i = 0; i < k.length; i++){
//     if(k[i].indexOf('a') != -1){
//         console.log(k[i]);
//     }
// }
// function modul (x){
//     if (x >0)
//     {
//         return x;
//     }
//     return (x > 0)? x : (x ! ==0)? -x: 0;
// }

// function sum (a,b){
//     return a + b;
// }

// console.log(sum(2, 3));
// console.log(sum(2, 3));
// console.log(sum(2, 3));

// function greet ( name){
//     console.log(helo word${name}!);
// }


// let k =[1,3,4,5,6];
// function arrayprint(x){
//     for (const y of x){
//         console.log(y);
//     }
// }
// arrayprint(k);


// let k=[91,2,-4,5];
// function arrayInFindNumber(x,j){
//     for (const y of x){
//         if (j === y){
//             return true;
//         }
//     }
//     return false;
// }
// console.log(arrayInFindNumber(k, -4));



// function max (...x){
//     let katta =x [0];
//     for (const y of x){
//         if (katta < y){
//             katta =y;
//         }
//     }
//     return katta ;
// }
// console.log(max(5,12,-10,45));


// let s= "men darsga keldim";
// console.log (s.substring(5,100));


// let gap = "men darsga kech qoldim";
// let start = 4;
// let end = 20;

// let natija = gap.slice(start, end);
// console.log(natija);
// function cals(n){
//     if (n>0){
//         return n + cals(n-1);
//     }
//     return 0;
// }
// let s= cals (11)
// console.log(s)



// let n=100;
// let count =0;
// while (n !==0){
//     count++;
//     n=parseInt(n/10);
// }
// console.log(count);



// let count= 0;
// function countDigit(n){
//     if (n !==0){
//         count++;
//         n=countDigit(parseInt(n/10));
//     }
//     return(count ===0)? 1 : count++;

// }
// let k =countDigit(n);
// console.log(k);



// let vv=[1,3,5,7,17];
// console.log(typeof vv)



// const car ={
//     model:"Mazda",
//     year:"2026",
//     speed:"200",
//     color:"yellow",
// };
// console.log(car);



// const student ={
//     name:"",
//     fam:"",
//     age:"",
//     university:"",
// }
// student.name="Ali";
// student.fam="Jabbarov";
// student.age="19";
// student.university="PDP";
// console.log(student);




// let car = {
//     speed: 60
// };
// let radar = {
//     calculateFine: function(speed) {
//         if (speed > 60 && speed < 80) {
//             return 412000;
//         } else if (speed >= 80 && speed < 120) {
//             return 824000;
//         } else if (speed >= 120) {
//             return 1648000;
//         } else {
//             return 0;
//         }
//     }
// };

// let fine = radar.calculateFine(car.speed);

// console.log("Tezlik:", car.speed);
// console.log("Jarima:", fine);
// [04.06.2026 19:25] Umid: const express = require('express');
// const app = express();
// const fs = require('fs');
// const {JSDOM} = require('jsdom');


// const port = process.env.PORT || 3000;

// const rf = fs.readFileSync('./index.html', 'utf-8');

// const dom = new JSDOM(rf);
// const document = dom.window.document;

// const name = 'Davronbek';
// const box_id = document.getElementById('box_id');

// app.get ('/', (req, res) => {
//     const h1 = document.createElement('h1');
//     h1.innerHTML = name;
//     box_id.appendChild(h1);
//     res.send(dom.serialize());
// })

// app.listen(port, () => {
//     console.log(Listening on port ${port});
// })