from sqlalchemy import text

from common.delete_flg import DELETE_FLG
from dao.TblUsersDAO import TblUsersDAO
from db.Orm import Orm

# from passlib.hash import sha256_crypt
import bcrypt

from entity.TblUsers import TblUsers

conn = Orm()
tblUsersDAO = TblUsersDAO()

# salt = b'uvfXzF34290'


def createUser(user_full_name, user_email, user_password):
    try:
        # user_password = sha256_crypt.encrypt(user_password)
        salt = bcrypt.gensalt()
        user_password = user_password.encode('utf-8')
        user_password = bcrypt.hashpw(user_password, salt)
        user_password = user_password.decode('utf8')
        print(user_password)

        # conn.get_session().execute("INSERT INTO tbl_users(full_name, email, password) Values(%s, %s, %s);",
        #                            (user_full_name, user_email, user_password,))
        # conn.get_session().commit()
        user = TblUsers()
        user.__init__(full_name=user_full_name,
                      email=user_email,
                      password=user_password,
                      delete_flg=DELETE_FLG.NONE_DELETE)
        tblUsersDAO.insert_or_update(user)
    except Exception as e:
        print(e)
        return 0

    return 1


def checkUser(login_email, login_password):
    sql = 'SELECT password FROM tbl_users WHERE email = :email'
    user = conn.get_session().execute(text(sql), {'email': login_email}).fetchone()
    # user = conn.get_connection().fetchone()

    try:
        # if not sha256_crypt.verify(user[0], login_password):
        check = login_password.encode('utf-8')
        hashed_password = str(user[0]).strip()
        hashed_password = hashed_password.encode('utf-8')
        if not bcrypt.checkpw(check, hashed_password):
            return 0
        else:
            return 1
    except Exception as e:
        print(e)
        return 0
