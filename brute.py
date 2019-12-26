import crypt
salt = '$6$YwOUDqo2$'
passwd_hash = '97qchduVQjoESS2Hl953nh18uI7gMcrY7h5OfQKcfWK4VjIi.TiJ9DiZmMYQU4TmLOvz/V4nkrvmZ3a6wbRmw1'
with open ( '10000_most_common_passwords.txt' ) as h :
 for l in h . readlines ():
    passwd = l . rstrip ()
    if ( crypt . crypt ( passwd , salt ) == salt + passwd_hash ):
	print ' Password : ' + passwd
	break
