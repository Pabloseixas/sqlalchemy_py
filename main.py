from sqlalchemy import create_engine, Table, Column, Integer, String, Date, Boolean, MetaData, select, text, Float
import logging, os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Iniciando o programa')

#comunicação entre p
from segurança import get_engine

engine = get_engine()

# Resto do seu código...


metadata = MetaData()

# Definição da tabela Cliente
cliente = Table('Cliente', metadata,
                Column('ID', Integer, primary_key=True),
                Column('Nome', String(100)),
                Column('CPF', String(14)),
                Column('DataNascimento', Date),
                Column('EstadoCivil', String(10)),
                Column('TemFilhos', Boolean),
                Column('Telefone', String(15)),
                Column('Email', String(100)),
                Column('TipoCliente', String(10))
                )

# Definição da tabela Fornecedor
fornecedor = Table('Fornecedor', metadata,
                   Column('ID', Integer, primary_key=True),
                   Column('Nome', String(100)),
                   Column('Telefone', String(15)),
                   Column('Email', String(100)),
                   Column('Endereco', String(200))
                   )

# Definição da tabela Produto
produto = Table('Produto', metadata,
                Column('ID', Integer, primary_key=True),
                Column('Nome', String(100)),
                Column('Descricao', String(200)),
                Column('Preco', Float()),
                Column('QuantidadeEstoque', Integer),
                Column('FornecedorID', Integer)
                )

# Definição da tabela Pedido
pedido = Table('Pedido', metadata,
               Column('ID', Integer, primary_key=True),
               Column('Data', Date),
               Column('ClienteID', Integer)
               )

# Definição da tabela ItemPedido
item_pedido = Table('ItemPedido', metadata,
                    Column('ID', Integer, primary_key=True),
                    Column('Quantidade', Integer),
                    Column('Preco', Float()),
                    Column('ProdutoID', Integer),
                    Column('PedidoID', Integer)
                    )

# Criação de todas as tabelas
metadata.create_all(engine)

# Exemplo de como acessar dados na tabela Cliente
with engine.connect() as connection:
    result = connection.execute(select(cliente))
    for row in result:
        logger.info(row)

print()