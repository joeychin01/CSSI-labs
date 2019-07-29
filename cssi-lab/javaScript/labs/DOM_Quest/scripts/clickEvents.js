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

console.log("Running Click Events Script");

let box1 = document.querySelector("#box1");
let box2 = document.querySelector("#box2");
let box3 = document.querySelector("#box3");
let box4 = document.querySelector("#box4");
let box5 = document.querySelector("#box5");

const changeOtherColor = (color) => {
  box1.style.backgroundColor = color
  box2.style.backgroundColor = color;
  box3.style.backgroundColor = color;
}

box1.addEventListener("click", () => {
  let color = box1.style.backgroundColor;
  changeOtherColor(box1.style.backgroundColor);
  console.log(box1.style.backgroundColor);
  console.log(color);
});
box2.addEventListener("click", () => {
  let color = box1.style.color;
  console.log(color);
  box1.style.backgroundColor = "pink";
  box2.style.backgroundColor = "pink";
  box3.style.backgroundColor = "pink";
});
box3.addEventListener("click", () => {
  let color = box1.style.color;
  console.log(color);
  box1.style.backgroundColor = "orange";
  box2.style.backgroundColor = "orange";
  box3.style.backgroundColor = "orange";
});

let color4 = false;
let color5 = true;

box4.addEventListener("click", () => {
  if(color4)
  {
    box4.style.backgroundColor = "yellow";
    color4 = false;
  }
  else {
    box4.style.backgroundColor = "blue"
    color4 = true;
  }
});
box5.addEventListener("click", () => {
  if(color5){
    box5.style.backgroundColor = "yellow";
    color5 = false;

  }
  else {
    box5.style.backgroundColor = "blue"
    color5 = true;
  }
});
