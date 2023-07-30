from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column, Enum

from common.delete_flg import DELETE_FLG

Base = declarative_base()


class TblUsers(Base):
    __tablename__ = "tbl_users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)
    delete_flg = Column(Enum(DELETE_FLG))

    def __new__(cls):
        return super().__new__(cls)

    def __init__(self,
                 full_name: str = None,
                 email: str = None,
                 password: str = None,
                 delete_flg: DELETE_FLG = DELETE_FLG) -> None:
        self.full_name = full_name
        self.email = email
        self.password = password
        self.delete_flg = delete_flg
