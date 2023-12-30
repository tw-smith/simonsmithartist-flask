




const openMenuIcon = document.getElementById('openIcon');
const closeMenuIcon = document.getElementById('closeIcon');
const bodyElement = document.getElementsByTagName("body")[0]

const navMenu = document.getElementById("navMenu");
const navIcon = document.getElementById("navIcon")
const navCloseIcon = document.getElementById("navCloseIcon")
navIcon.addEventListener('click', toggleNavMenu)


const cartDetail = document.getElementById("cartDetail")
const cartIcon = document.getElementById("cartIcon")
const cartCloseIcon = document.getElementById("cartCloseIcon")
cartIcon.addEventListener('click', toggleCartDetail)


function toggleNavMenu() {
    if (navMenu.classList.contains("showModal")) {
        navMenu.classList.toggle("showModal");
        navCloseIcon.style.display = "none";
        openMenuIcon.style.display = "block";
        bodyElement.classList.toggle("preventScroll")
    } else {
        navMenu.classList.toggle("showModal")
        navCloseIcon.style.display = "block";
        openMenuIcon.style.display = "none";
        bodyElement.classList.toggle("preventScroll");
    }
}

async function toggleCartDetail() {
    if (cartDetail.classList.contains("showModal")) {
        cartDetail.classList.toggle("showModal");
        cartCloseIcon.style.display = "none";
        openMenuIcon.style.display = "block";
        bodyElement.classList.toggle("preventScroll")
    } else {
        const cart = getCartContents()
        cartDetail.classList.toggle("showModal")
        cartCloseIcon.style.display = "block";
        openMenuIcon.style.display = "none";
        bodyElement.classList.toggle("preventScroll");
        console.log(JSON.stringify(cart))
        document.getElementById("cartContents").innerText = cart
    }
}

async function getCartContents() {
    fetch('/cart').then(response =>
        response.json().then(data => ({
            data: data,
            status: response.status
        })).then(res => {
            console.log(res.status, res.data)

        }))
        return res.data



   // const contents = await fetch('/cart')
   //  console.log(contents)
   //  return contents.json()
}



