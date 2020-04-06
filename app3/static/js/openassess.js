let main=()=>{
    let assess;
  
    document.querySelector('.close-btn').addEventListener('click',(e)=>{
        e.target.parentNode.parentNode.parentNode.classList.add('modal__dispnone');
    });
    /*
    document.querySelector('.fa-plus').addEventListener('click',(e)=>{
        console.log( document.querySelector('.modal'));
       document.querySelector('.modal').classList.toggle('modal__dispnone'); 
    });*/
    assess=document.querySelectorAll('.asessment');
    assess.forEach(ele=>{
        ele.addEventListener('click',(e)=>{    
            document.querySelector('.modal').classList.toggle('modal__dispnone'); 
        })
    })
}
main();

function togglenav(){
    document.querySelector('.nav-btn').addEventListener('click',()=>{
        document.querySelector('.navbar').classList.toggle('show-navbar');
    });
}
togglenav();