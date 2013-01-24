from dbConfiguration import engine, Session, Base
from Users import randomUser
from Products import Product

def populate(session, number = 1000):
    for _ in xrange(number):
        usr = randomUser()
        print usr
        session.add(usr)

def createProducts(session):
    prods = [Product(u'Notebook Pear',                        u'Informatica',                  3500),
             Product(u'Notebook HAL' ,                        u'Informatica',                  2500),
             Product(u'Celular Pear youPhone',                u'Telefonia',                    1800),
             Product(u'Celular Blue Robot',                   u'Telefonia',                    1600),
             Product(u'Celular youClone com 8 chips',         u'Telefonia',                     500),
             Product(u'Celular ScritorioPhone for Business',  u'Telefonia',                    1200),
             Product(u'Tenis Mike',                           u'Roupas e Acessorios',           300),
             Product(u'Tenis Rei',                            u'Roupas e Acessorios',           150),
             Product(u'Earphone youPhone original',           u'Acessorios de Informatica',     90),
             Product(u'Mouse CheapJunk Systems',              u'Acessorios de Informatica',      5),
             Product(u'Mouse MacroHard sem fio',              u'Acessorios de Informatica',     90),
             Product(u'CD "Live Acustico" de Boy Band',       u'Musica',                        25),
             Product(u'CD "Cool Jazz" de Km Davis',           u'Musica',                        25),
             Product(u'Fraldas Pimpolho - 200 unidades',      u'Bebe',                          50),
             Product(u'Carrinho de Bebe Heracles',            u'Bebe',                         150),
             Product(u'Cerveja Deva - 6 pack',                u'Alimentos e Bebidas',           15),
             Product(u'Vinho Petit Chateau Verdot',           u'Alimentos e Bebidas',          150),
             Product(u'Jogo - God of Battle',                 u'Jogos',                         50),
             Product(u'Livro "Receitas para Solteiros"',      u'Livros',                        25),
             Product(u'Livro "God of Battle - Estrategias"',  u'Livros',                        25),
             Product(u'Livro "Como Nao Matar o Seu Bebe: a Arte da Guerra para pais solteiros"', u"Livros", 25),
             Product(u'Livro "Espeleologia Comparada: Introducao ao Calculo Setorial Multiplexado"', u'Livros', 50)]
    session.add_all(prods)
    prods = list(session.query(Product))
    return prods

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    objs = createProducts(session)
    populate(session, number = 1000)
    session.commit()
    session.close()
