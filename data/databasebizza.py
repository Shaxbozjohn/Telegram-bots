import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, BIGINT, Sequence
from data.config import POSTGRES_URI
from sqlalchemy import table
import sqlalchemy



engine = create_engine(POSTGRES_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)



class User(Base):
    __tablename__ = "users"
    full_name = Column(String)
    user_id = Column(BIGINT, primary_key=True)
    data_register = Column(String)



async def add_user(full_name,  user_id, data_register):
    session = Session()


    user = User(full_name=full_name,
                user_id=user_id,
                data_register = datetime.datetime.now()
    )


    session.add(user)
    session.commit()
    session.close()


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,Sequence('products_seq'), primary_key=True)
    product_name = Column(String)
    product_price = Column(Integer)

class Basket(Base):
   __tablename__ = 'basket'

   id = Column(Integer, primary_key=True)
   product_id = Column(Integer, sqlalchemy.ForeignKey('product.id'))
   product = relationship(Product)

   # user_id = user_





def add_pro1(product_name, product_price):

    if isinstance(product_name, str) and isinstance(product_price, int):

        session = Session()
        new_product = Product(
            product_name=product_name,
            product_price=product_price

        )
        session.add(new_product)
        session.commit()
        session.close()



    else:
        return "Error"


Base.metadata.create_all(bind=engine)
