function togglenav(){
    document.querySelector('.nav-btn').addEventListener('click',()=>{
        document.querySelector('.navbar').classList.toggle('show-navbar');
    });
}
togglenav();