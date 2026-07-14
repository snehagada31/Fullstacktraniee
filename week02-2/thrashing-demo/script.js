const container = document.getElementById("container");

function createBoxes(){

    if(container.children.length > 0) return;

    for(let i=0;i<100;i++){

        const box=document.createElement("div");

        box.className="box";

        container.appendChild(box);

    }

}

// ------------------
// Before
// ------------------

function runBefore(){

    const boxes=document.querySelectorAll(".box");

    boxes.forEach(box=>{

        box.style.width="100px";

        box.offsetHeight;

        box.style.height="100px";

    });

}

// ------------------
// After
// ------------------

function runAfter(){

    const boxes=document.querySelectorAll(".box");

    const heights=[];

    boxes.forEach(box=>{

        heights.push(box.offsetHeight);

    });

    boxes.forEach(box=>{

        box.style.width="100px";

        box.style.height="100px";

    });

}