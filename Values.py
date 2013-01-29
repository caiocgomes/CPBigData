from EntityDefinitions import Product
from LogOdds import LogOddsCalculator

nbPear   = Product(u'Notebook Pear', u'Informatica', 3500)
nbHal    = Product(u'Notebook HAL', u'Informatica', 2500)
youPhone = Product(u'Celular Pear youPhone', u'Telefonia', 1800)
robot    = Product(u'Celular Blue Robot', u'Telefonia', 1600)
youClone = Product(u'Celular youClone com 8 chips', u'Telefonia', 500)
busPhone = Product(u'Celular ScritorioPhone for Business', u'Telefonia', 1200)
mike     = Product(u'Tenis Mike', u'Roupas e Acessorios', 300)
rei      = Product(u'Tenis Rei', u'Roupas e Acessorios', 150)
earphone = Product(u'Earphone youPhone original', u'Acessorios de Informatica', 90)
mouseChp = Product(u'Mouse CheapJunk Systems', u'Acessorios de Informatica', 5)
mouseMH  = Product(u'Mouse MacroHard sem fio', u'Acessorios de Informatica', 90)
boyBand  = Product(u'CD "Live Acustico" de Boy Band', u'Musica', 25)
jazz     = Product(u'CD "Cool Jazz" de Km Davis', u'Musica', 25)
fraldas  = Product(u'Fraldas Pimpolho - 200 unidades', u'Bebe', 50)
carrinho = Product(u'Carrinho de Bebe Heracles', u'Bebe', 150)
cerveja  = Product(u'Cerveja Deva - 6 pack', u'Alimentos e Bebidas', 15)
vinho    = Product(u'Vinho Petit Chateau Verdot', u'Alimentos e Bebidas', 150)
godBatt  = Product(u'Jogo - God of Battle', u'Jogos', 50)
receitas = Product(u'Livro "Receitas para Solteiros"', u'Livros', 25)
godLivro = Product(u'Livro "God of Battle - Estrategias"',  u'Livros', 25)
livroPai = Product(u'Livro "Como Nao Matar o Seu Bebe: a Arte da Guerra para pais solteiros"', u"Livros", 25)
livroEsp = Product(u'Livro "Espeleologia Comparada: Introducao ao Calculo Setorial Multiplexado"', u'Livros', 50)

prods = [nbPear, nbHal, youPhone, robot, youClone, busPhone, mike, rei, earphone, mouseChp, mouseMH, boyBand, jazz, fraldas, carrinho, cerveja, vinho, godBatt, receitas, godLivro, livroPai, livroEsp]

baseLodd = 1.0
LOdds = LogOddsCalculator()

LOdds[nbPear, 'usrIncome', 1] = baseLodd
LOdds[nbPear, 'usrIncome', 2] = 2 * baseLodd
LOdds[nbPear, 'usrAge', 0] = 2 * baseLodd
LOdds[nbPear, 'usrAge', 1] = baseLodd
LOdds[nbPear, nbHal] = -baseLodd

LOdds[nbHal, 'usrAge', 2] = baseLodd
LOdds[nbHal, 'usrIncome', 1] = baseLodd
LOdds[nbHal, 'usrIncome', 2] = 2 * baseLodd

LOdds[youPhone, 'usrIncome', 1] = baseLodd
LOdds[youPhone, 'usrIncome', 2] = 2 * baseLodd
LOdds[youPhone, nbPear] = baseLodd
LOdds[youPhone, robot] = -3*baseLodd
LOdds[youPhone, youClone] = -3*baseLodd
LOdds[youPhone, busPhone] = -3*baseLodd

LOdds[robot, 'usrIncome', 1] = baseLodd
LOdds[robot, 'usrAge', 1] = baseLodd
LOdds[robot, nbHal] = baseLodd
LOdds[robot, youClone] = -3*baseLodd
LOdds[robot, busPhone] = -3*baseLodd

LOdds[youClone, 'usrIncome', 0] = 2 * baseLodd
LOdds[youClone, 'usrIncome', 1] = - baseLodd
LOdds[youClone, 'usrIncome', 2] = - 3 * baseLodd
LOdds[youClone, busPhone] = -3*baseLodd

LOdds[busPhone, 'usrSex', 'M'] = baseLodd
LOdds[busPhone, 'usrAge', 2] = baseLodd
LOdds[busPhone, 'usrAge', 3] = baseLodd

LOdds[mike, 'usrAge', 0] = 1.5 * baseLodd
LOdds[mike, 'usrAge', 1] = baseLodd
LOdds[mike, 'usrIncome', 1] = baseLodd
LOdds[mike, 'usrIncome', 2] = baseLodd
LOdds[mike, 'usrIncome', 0] = -baseLodd
LOdds[mike, rei] = -3 * baseLodd

LOdds[rei, 'usrIncome', 0] = baseLodd

LOdds[earphone, youPhone] = 3 * baseLodd
LOdds[earphone, robot] = -3 * baseLodd

LOdds[mouseChp, nbHal, 'usrIncome', 0] = 1 * baseLodd
LOdds[mouseChp, 'usrIncome', 2] = -baseLodd
LOdds[mouseChp, mouseMH] = - baseLodd
LOdds[mouseMH, nbHal] = baseLodd
LOdds[mouseMH, nbHal, 'usrIncome', 2] = baseLodd

LOdds[boyBand, 'usrSex', 'F'] =  baseLodd
LOdds[boyBand, 'usrAge', 0] =  baseLodd
LOdds[boyBand, 'usrEdu', 0] =  baseLodd
LOdds[boyBand, 'usrEdu', 1] =  -baseLodd
LOdds[boyBand, 'usrEdu', 2] =  -baseLodd
LOdds[boyBand, 'usrSex', 'M'] = -3 * baseLodd
LOdds[boyBand, 'usrAge', 1] =  -1 * baseLodd
LOdds[boyBand, 'usrAge', 2] =  -2 * baseLodd
LOdds[boyBand, 'usrAge', 3] =  -3 * baseLodd


LOdds[jazz, 'usrSex', 'M'] = 0.5 * baseLodd
LOdds[jazz, 'usrAge', 3] = 2*baseLodd
LOdds[jazz, 'usrAge', 2] = baseLodd
LOdds[jazz, 'usrEdu', 2] = baseLodd
LOdds[jazz, 'usrIncome', 2] = baseLodd

LOdds[fraldas, 'usrAge', 1] = 0.50 * baseLodd
LOdds[fraldas, 'usrAge', 2] = 0.75 * baseLodd
LOdds[fraldas, 'usrSex', 'F'] = 0.75 * baseLodd
LOdds[fraldas, nbPear] = -0.5 * baseLodd

LOdds[carrinho, fraldas] = 500 * baseLodd
LOdds[cerveja, fraldas] = 0.5 * baseLodd
LOdds[cerveja, 'usrSex', 'M'] = 3 * baseLodd
LOdds[cerveja, livroPai, 'usrSex', 'M'] = 2*baseLodd

LOdds[vinho, cerveja] = -0.5 * baseLodd
LOdds[vinho, jazz] = 2 * baseLodd
LOdds[vinho, 'usrIncome', 2] = 2 * baseLodd
LOdds[vinho, 'usrAge', 3] = 2 * baseLodd

LOdds[godBatt, 'usrAge', 0] = 3 * baseLodd
LOdds[godBatt, 'usrAge', 1] = baseLodd
LOdds[godBatt, 'usrAge', 3] = -3 * baseLodd
LOdds[godBatt, 'usrSex', 'M'] = baseLodd

LOdds[receitas, 'usrSex', 'M'] = 2 * baseLodd
LOdds[receitas, 'usrAge', 1] = 3 * baseLodd
LOdds[receitas, cerveja] = 3 * baseLodd
LOdds[receitas, 'usrAge', 2] = -baseLodd
LOdds[receitas, 'usrAge', 3] = -2*baseLodd


LOdds[godLivro, godBatt] = 10 * baseLodd
for prod in prods:
    if prod.prodid != godBatt.prodid:
        LOdds[godLivro, prod] = -10 * baseLodd

LOdds[livroPai, 'usrSex', 'M'] = baseLodd
LOdds[livroPai, 'usrSex', 'F'] = -baseLodd
LOdds[livroPai, fraldas, 'usrSex', 'M'] = 10*baseLodd
LOdds[livroPai, carrinho, 'usrSex', 'M'] = 10*baseLodd
LOdds[livroPai, fraldas] = 2*baseLodd
LOdds[livroPai, carrinho] = 2*baseLodd
LOdds[livroPai, 'usrAge', 1] = baseLodd
LOdds[livroPai, carrinho, 'usrSex', 'M'] = 5*baseLodd

LOdds[livroEsp, 'usrEdu', 0] = -2 * baseLodd
LOdds[livroEsp, 'usrEdu', 1] = -1 * baseLodd
LOdds[livroEsp, 'usrEdu', 1] =  baseLodd
LOdds[livroEsp, 'usrEdu', 1] =  baseLodd
