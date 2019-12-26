import crypt
salt = '$6$mTSKM5AffXDwoY05$'
passwd_hash = 'HsxG09ja2NZsJH0GORAHv8Fkt1PdYlfrFXgH/CyUXrk/FeFlLJX88893qSHNLhE9H7N5z/K86LJFeFwitRhp2'
with open ( '10000_most_common_passwords.txt' ) as h :
 for l in h . readlines ():
    passwd = l . rstrip ()
    if ( crypt . crypt ( passwd , salt ) == salt + passwd_hash ):
	print ' Password : ' + passwd
	break
