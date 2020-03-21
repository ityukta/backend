let main=()=>{
    let btn;
    document.querySelector('.teacherli').addEventListener('click',(e)=>{
        e.preventDefault();
        document.querySelector('.sub').classList.toggle('show');
    });
    document.querySelector('.studentli').addEventListener('click',(e)=>{
        e.preventDefault();
        document.querySelector('.studentlist').classList.toggle('show');
    });
    document.querySelector('.close-btn').addEventListener('click',(e)=>{
        e.target.parentNode.parentNode.parentNode.classList.add('modal__dispnone')
    });
    /*document.querySelector('.fa-plus').addEventListener('click',(e)=>{
        console.log( document.querySelector('.modal'));
       document.querySelector('.modal').classList.toggle('modal__dispnone'); 
    });*/
    document.querySelectorAll('.assignclass__add__pic').forEach(ele=>{
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
