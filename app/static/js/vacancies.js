document.addEventListener('DOMContentLoaded', async () => {
    let page = 0
    let totalPages

    try {
        let response = await fetch(`/api/vacancies/${page}`)
        let data = await response.json()
        let vacanciesSection = document.querySelector('.vacancies')
        totalPages = data.total_pages

        data.vacancies.forEach(vacancy => {
            let card = document.createElement('div')
            card.classList.add('vacancy', 'tile', 'is-parent')
            card.innerHTML = `
                <article class="tile is-child box">
                    <div class="level">
                        <p class="title"><a href=${vacancy.url}>${vacancy.name}</a></p>
                        <img src="${vacancy.employer.logo}" alt="${vacancy.employer.name}"/>
                    </div>
                    <div class="content">
                        ${vacancy.responsibility ? `<p class="description">${vacancy.responsibility}</p>` : '<p class="description">Описание отсутствует</p>'}
                        ${vacancy.salary ? `<p class="salary">
                            ${vacancy.salary.from ? `<span class="salary-from">от ${vacancy.salary.from} </span>` : ''}
                            ${vacancy.salary.to ? `<span class="salary-from">до ${vacancy.salary.to}</span>` : ''}
                            <span class="salary-currency"> ${vacancy.salary.currency}</span>
                        </p>` : '<span class="salary-no">З/п не указана</span>'}
                    </div>
                </article>`

            vacanciesSection.prepend(card)
        });
    } catch(err) {
        console.log(err)
    }

    document.querySelector('.button__show-more').addEventListener('click', async () => {
        page += 1

        try {
            let response = await fetch(`/api/vacancies/${page}`)
            let data = await response.json()
            let vacanciesSection = document.querySelector('.vacancies')

            data.vacancies.forEach(vacancy => {
                let card = document.createElement('div')
                card.classList.add('vacancy', 'tile', 'is-parent')
                card.innerHTML = `
                    <article class="tile is-child box">
                        <div class="level">
                            <p class="title"><a href=${vacancy.url}>${vacancy.name}</a></p>
                            <img src="${vacancy.employer.logo}" alt="${vacancy.employer.name}"/>
                        </div>
                        <div class="content">
                            ${vacancy.responsibility ? `<p class="description">${vacancy.responsibility}</p>` : ''}
                            ${vacancy.salary ? `<p class="salary">
                                ${vacancy.salary.from ? `<span class="salary-from">от ${vacancy.salary.from} </span>` : ''}
                                ${vacancy.salary.to ? `<span class="salary-from">до ${vacancy.salary.to}</span>` : ''}
                                <span class="salary-currency"> ${vacancy.salary.currency}</span>
                            </p>` : '<span class="salary-no">З/п не указана</span>'}
                        </div>
                    </article>`

                vacanciesSection.append(card)
            });
        } catch(err) {
            console.log(err)
        }

        if (page === totalPages - 1) {
            document.querySelector('.button__show-more').remove()
        }
    })
})