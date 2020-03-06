async function addFavorite(id, el) {
    let res = await fetch(`/api/vacancies/favorite/${id}`)

    if (res.statusText !== 'OK') location.href = '/login'

    el.classList.add('is-info')
    el.innerHTML = 'В избранном'
}

document.addEventListener('DOMContentLoaded', async () => {
    let page = 0
    let totalPages
    let buttonShowMore = document.querySelector('.button__show-more')
    let vacanciesSection = document.querySelector('.vacancies')
    let jsonData = []

    let createVacancyTile = (vacancy) => {
        let card = document.createElement('div')

        card.classList.add('vacancy', 'tile', 'is-parent')
        card.innerHTML = `
            <article class="tile is-child box">
                <div class="level">
                    <p class="title"><a href=${vacancy.url}>${vacancy.name}</a></p>
                    <img src="${vacancy.employer.logo}" alt="${vacancy.employer.name}" loading="lazy"/>
                </div>
                <div class="content">
                    ${vacancy.responsibility ? `<p class="description">${vacancy.responsibility}</p>` : '<p class="description">Описание отсутствует</p>'}
                    ${vacancy.salary ? `<p class="salary has-text-weight-semibold">
                        ${vacancy.salary.from ? `<span class="salary-from">от ${vacancy.salary.from} </span>` : ''}
                        ${vacancy.salary.to ? `<span class="salary-from">до ${vacancy.salary.to}</span>` : ''}
                        <span class="salary-currency"> ${vacancy.salary.currency}</span>
                    </p>` : '<p class="salary has-text-weight-semibold"><span class="salary-no">З/п не указана</span></p>'}
                </div>
                ${jsonData.favorites.flat().includes(Number(vacancy.id)) ? `<button class="button is-small is-info">В избранном</button>` 
                : `<button class="button is-small" onclick="addFavorite(${vacancy.id}, this)">В избранное</button>`}
            </article>`

        vacanciesSection.append(card)
    }

    try {
        let response = await fetch(`/api/vacancies/${page}`)
        let data = await response.json()

        totalPages = data.total_pages

        document.querySelector('h1').innerHTML = `Найдено ${data.total_vacancies} вакансий` 

        jsonData = data

        data.vacancies.forEach(vacancy => createVacancyTile(vacancy));

        buttonShowMore.classList.remove('is-loading')
    } catch(err) {
        console.log(err)
    }

    buttonShowMore.addEventListener('click', async () => {
        page++
        buttonShowMore.classList.add('is-loading')

        try {
            let response = await fetch(`/api/vacancies/${page}`)
            let data = await response.json()

            data.vacancies.forEach(vacancy => createVacancyTile(vacancy))
        } catch(err) {
            console.log(err)
        }

        buttonShowMore.classList.remove('is-loading')

        if (page === totalPages - 1) {
            buttonShowMore.remove()
        }
    })

    
})
