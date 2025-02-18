# example:
# def check_user_in_db(did: int, req: Request, mariadb: Session = Depends(get_db)):
#     userdata = getUserBySession(req=req, mariadb=mariadb)
#     if not userdata:
#         raise LOGIN_REQUIRED
#     dbdata = mariadb.query(DB).filter(DB.id == did).first()
#     if not dbdata or dbdata.is_deleted:
#         raise DB_NOT_FOUND if not dbdata else DB_NOT_FOUND
#     dbjoin = DBJoinByUseridx(did=did, useridx=userdata[0].idx, mariadb=mariadb)
#     if not dbjoin:
#         raise USER_NOT_FOUND_IN_DB
#     return dbjoin[0]


# def check_valid_session(did: int, req: Request, mariadb: Session = Depends(get_db)):
#     userdata = getUserBySession(req=req, mariadb=mariadb)
#     if not userdata:
#         raise LOGIN_REQUIRED
#     return userdata[0]
