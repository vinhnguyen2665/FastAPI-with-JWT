from common import log
from db.Orm import Orm
from entity.TblUsers import TblUsers


class TblUsersDAO:
    db = None

    def __init__(self) -> None:
        self.db = Orm()
        super().__init__()

    # def find_list_database_info(self, conditions: BackupInfo):
    #     try:
    #         session = self.dbConnect.get_session()
    #         query = session.query(BackupInfo).where(BackupInfo.delete_flg == conditions.delete_flg)
    #
    #         result = query.all()
    #         # print(query)
    #         return result
    #     except Exception as e:
    #         log.error(e)

    # def insert(self, database_info: BackupInfo):
    #     try:
    #         session = self.dbConnect.get_session()
    #         session.add(database_info)
    #         session.commit()
    #     except Exception as e:
    #         log.error(e)

    def insert_or_update(self, tbl_users: TblUsers):
        try:
            session = self.db.get_session()
            session.merge(tbl_users)
            session.commit()
            session.flush()
        except Exception as e:
            log.error(e)
            raise e
