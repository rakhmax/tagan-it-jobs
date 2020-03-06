async function deleteFavorite(id, el) {
    let res = await fetch(`/api/favorites/delete/${id}`, {method: 'DELETE'})

    let vacanciesSection = document.querySelector('.vacancies')

    if (res.statusText !== 'OK') location.href = '/login'
    if (res.statusText === 'OK') {
        el.closest('.vacancy').remove()

        if (!vacanciesSection.hasChildNodes()) {
            vacanciesSection.innerHTML = `<h3>Пусто</h3>`
        }
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    let vacanciesSection = document.querySelector('.vacancies')
    
    let createVacancyTile = (vacancy) => {
        let card = document.createElement('div')

        card.classList.add('vacancy', 'tile', 'is-parent')
        card.innerHTML = `
            <article class="tile is-child box">
                <div class="level">
                    <p class="title"><a href=${vacancy.url}>${vacancy.name}</a></p>
                    <img src="${vacancy.employer.logo}" alt="${vacancy.employer.name}"/>
                </div>
                <div class="content">
                    ${vacancy.responsibility ? `<p class="description">${vacancy.responsibility}</p>` : '<p class="description">Подробнее на hh.ru</p>'}
                    ${vacancy.salary ? `<p class="salary has-text-weight-semibold">
                        ${vacancy.salary.from ? `<span class="salary-from">от ${vacancy.salary.from} </span>` : ''}
                        ${vacancy.salary.to ? `<span class="salary-from">до ${vacancy.salary.to}</span>` : ''}
                        <span class="salary-currency"> ${vacancy.salary.currency}</span>
                    </p>` : '<p class="salary has-text-weight-semibold"><span class="salary-no">З/п не указана</span></p>'}
                </div>
                <button class="button is-small" onclick="deleteFavorite(${vacancy.id}, this)">Удалить из избранного</button>
            </article>`

        vacanciesSection.append(card)
    }

    try {
        let response = await fetch(`/api/favorites`)
        let data = await response.json()

        if(data.msg === 'No vacancies') {
            vacanciesSection.innerHTML = `<h3>Пусто</h3>`
        } 

        data.forEach(vacancy => createVacancyTile(vacancy));
    } catch(err) {
        console.log(err)
    }
})