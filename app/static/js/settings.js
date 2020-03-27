document.addEventListener('DOMContentLoaded', () => {
    let buttonChangePass = document.querySelector('.button__changepass')

    document.querySelector('#changePassword').addEventListener("submit", async (e) => {
        e.preventDefault()
    
        document.querySelectorAll('.help').forEach(el => el.remove())
    
        buttonChangePass.classList.add('is-loading')
    
        try {
            let response = await fetch('/api/changepassword', { method: 'POST', body: new FormData(changePassword) })
            let data = await response.json()

            if (response.status === 409) {
                document.querySelector('.password')
                    .insertAdjacentHTML('beforeend', `<p class="help is-danger">${data.msg}</p>`)
                    buttonChangePass.classList.remove('is-loading')
                return
            } else if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`)
                buttonChangePass.classList.remove('is-loading')
                return
            } else {
                alert(data.msg)
                location.href = '/vacancies'
            }
        } catch(err) {
            console.error(err)
            buttonChangePass.classList.remove('is-loading')
        }

        buttonChangePass.classList.remove('is-loading')
    })
})