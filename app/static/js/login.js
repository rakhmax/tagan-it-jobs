document.addEventListener('DOMContentLoaded', () => {
    let buttonLogin = document.querySelector('.button__login')

    document.querySelector('#loginForm').addEventListener("submit", async (e) => {
        e.preventDefault()
    
        document.querySelectorAll('.help').forEach(el => el.remove())
    
        buttonLogin.classList.add('is-loading')
    
        try {
            let response = await fetch('/api/login', { method: 'POST', body: new FormData(loginForm) })
            let data = await response.json()
    
            if (response.status === 422) {
                document.querySelector('.email')
                    .insertAdjacentHTML('beforeend', `<p class="help is-danger">${data.msg}</p>`)
                return
            } else if (response.status === 409) {
                document.querySelector('.password')
                    .insertAdjacentHTML('beforeend', `<p class="help is-danger">${data.msg}</p>`)
                return
            } else if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`)
                return
            } else {
                location.href = '/favorites'
            }
        } catch(err) {
            console.error(err)
        }

        buttonLogin.classList.remove('is-loading')
    })
})
