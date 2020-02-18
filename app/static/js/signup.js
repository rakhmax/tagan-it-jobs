let agreement = document.querySelector('#agreement')
let buttonSubmit = document.querySelector('.button__submit')
let terms = document.querySelector('.terms')
let termsModal = document.querySelector('.modal')
let closeModal = document.querySelector('.button__close-modal')
let signupForm = document.querySelector('#signupForm')
let helps = document.querySelectorAll('.help')

agreement.addEventListener('change', () => {
    let isAgreementApplied = agreement.checked

    if (isAgreementApplied) {
        buttonSubmit.removeAttribute("disabled")
    } else {
        buttonSubmit.setAttribute("disabled", "")
    }
})

terms.addEventListener("click", () => {
    termsModal.classList.add('is-active')
})

closeModal.addEventListener('click', () => {
    termsModal.classList.remove('is-active')
})

.addEventListener("submit", async (e) => {
    e.preventDefault()

    helps.forEach(el => el.remove())
 
    try {
        let response = await fetch('/api/signup', { method: 'POST', body: new FormData(signupForm) })
        let data = await response.json()
        
        if (response.status === 422) {
            document.querySelector('.email')
                .insertAdjacentHTML('beforeend', `<p class="help is-danger">${data.msg}</p>`)
            return
        } else if (response.status === 409) {
            document.querySelector('.agreement')
                .insertAdjacentHTML('beforeend', `<p class="help is-danger">${data.msg}</p>`)
            return
        } else if (response.status !== 200) {
            console.log(`Looks like there was a problem. Status code: ${response.status}`)
            return
        }
    } catch(err) {
        console.error(err)
    }

    try {
        let response = await fetch('/api/login', { method: 'POST', body: new FormData(signupForm) })
        let data = await response.json()

        if (response.status === 422) {
            document.querySelector('.email')
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
})