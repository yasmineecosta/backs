//alert('Olá, seja bem vindo!') // Olá, seja bem vindo!

async function carregarAnimais(){
    //console.log('carregando animais')
    //axios.get('http://127.0.0.1:8000/animais').then(response => console.log(response.data))
    const response = await axios.get('http://127.0.0.1:8000/animais')
    //console.log(response.data)

    const animais = response.data
    const lista = document.getElementById('Lista-animais')
    
    lista.innerHTML = ''
    animais.forEach(animal=>{
        const item = document.createElement('li')

        const linha = `${animal.nome} - idade: ${animal.idade} - sexo: ${animal.sexo} - cor: ${animal.cor}`
        // item.innerText = animal.nome
        item.innerText = linha
        lista.appendChild(item)
    })
    //const item = document.createElement('li')
    //item.innerText = 'Brie'
    //lista.appendChild(item)
}

function manipularFormulario(){
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')
    
    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value
        
        alert(`Formulario enviado... ${nome_animal}`)

        await axios.post('http://127.0.0.1:8000/animais', {
            id: 'sygd0',
            nome: nome_animal,
            idade: 2,
            sexo: 'femea',
            cor: 'branco'
        })
        alert('Animal cadastrado...')
    }
    
}

function app(){
    console.log('App iniciada')
    carregarAnimais()
    manipularFormulario()
}

document.addEventListener('DOMContentLoaded', () => {
    app();
}); // app iniciada