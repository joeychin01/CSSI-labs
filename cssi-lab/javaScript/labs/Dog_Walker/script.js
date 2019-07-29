

// // Copyright 2018 Google LLC
// //
// // Licensed under the Apache License, Version 2.0 (the "License");
// // you may not use this file except in compliance with the License.
// // You may obtain a copy of the License at
// //
// //      http://www.apache.org/licenses/LICENSE-2.0
// //
// // Unless required by applicable law or agreed to in writing, software
// // distributed under the License is distributed on an "AS IS" BASIS,
// // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// // See the License for the specific language governing permissions and
// // limitations under the License.
// const printAppt = (name, time) => {
//   if(checker(name))
//   {
//     console.log("I will walk " + name + " at 8pm");
//   }
//   else {
//     console.log("I will walk " + name + " at " + time);
//   }
// }
//
// const checker = (name) => {
//   if(name.charAt(0) == "a" || name.charAt(0) == "A")
//   {
//     return true;
//   }
//   return false;
// }
//
// // Task 1
// const dogName1 = "adam";
// const dogType1 = "beagle";
// printAppt(dogName1, "12:00pm");
// // Complete Task 1 Below
//
//
//
// const dogName2 = "Joe";
// const dogType2 = "bulldog";
//
// // Complete Task 2 Below
// if (dogType2 == "corgi") {
//   printAppt(dogName2, "12:00pm");
// } else {
//   printAppt(dogName2, "1:00pm");
// }
//
//
// const dogName3 = "Lola";
// const dogType3 = "poodle";
//
// // Complete Task 3 Below
// if (dogType3 == "corgi" || dogType3 == "beagle") {
//   printAppt(dogName3, "12:00pm");
// } else if (dogType3 == "bulldog") {
//   printAppt(dogName3, "1:00pm");
// } else {
//   printAppt(dogName3, "2:00pm");
// }
//
// console.log("hello there");
//
// let dogOwner = prompt("Enter your dog's name");
// dogOwner = dogOwner.toLowerCase();
// if (dogOwner == "spike") {
//   console.log("wow you're cool");
// } else {
//   console.log("haha you loser");
// }


const func = () => {
  console.log("hello there");
}
func();

setInterval(() => {
  console.log("hello there");
}, 100000);
