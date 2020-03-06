document.addEventListener('DOMContentLoaded', () => {
    let buttonLogout = document.querySelector('.button__logout')
    let navbarBurger = document.querySelector('.navbar-burger')
    let navbar = document.getElementById('navbar')


    navbarBurger.addEventListener('click', () => {
        navbar.classList.toggle('is-active')
    })

    if (buttonLogout) {
        buttonLogout.addEventListener('click', async e => {
            try {
                let response = await fetch('/api/logout', {method: 'POST'})
                let data = response.json()
        
                if (response.status !== 200) {
                    console.log(`Looks like there was a problem. Status code: ${response.status}`)
                    return
                } else {
                    location.href = '/'
                }
            } catch (error) {
                console.log(error)
            }
        })
    }
})
