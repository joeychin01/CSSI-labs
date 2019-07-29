// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let box6 = document.querySelector("#box6");
let rect = document.querySelector("#rect");
let title = document.querySelector("#title");

console.log("Running Window Events Script");

window.addEventListener("keypress", (e) => {
  console.log(e.keyCode);
});

window.addEventListener("keypress", (e) => {
if(e.keyCode == 97){
    box6.style.borderRadius = "50%";
  }
});

// window.addEventListener("scroll", () => {
// if(document.body.scrollTop > 1){
//     console.log("hello");
//   }
// });
window.addEventListener('scroll',function() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
            rect.style.backgroundColor = "black";
            title.innerHTML = "You are a master of DOM!";
        }
    else {
      rect.style.backgroundColor = "tomato";
      title.innerHTML = "";
    }
});
