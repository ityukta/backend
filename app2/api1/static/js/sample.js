let main=()=>{
    document.querySelector('.teacherli').addEventListener('click',(e)=>{
        e.preventDefault();
        document.querySelector('.sub').classList.toggle('show');
    });
    document.querySelector('.studentli').addEventListener('click',(e)=>{
        e.preventDefault();
        document.querySelector('.studentlist').classList.toggle('show');
    });
}
main();

function togglenav(){
    document.querySelector('.nav-btn').addEventListener('click',()=>{
        document.querySelector('.navbar').classList.toggle('show-navbar');
    });
}
togglenav();
