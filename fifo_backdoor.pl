use strict ;
use POSIX qw ( mkfifo );
use Fcntl qw ( O_RDWR O_RDONLY O_NONBLOCK );
my % h = ( ' IN ' = > [ '/ tmp / in_fifo ' , O_RDONLY , undef ], 
' OUT ' = > [ '/ tmp / out_fifo ' , O_RDWR , undef ]);
foreach my $v ( values % h )
{
	mkfifo ( $v - >[0] , 0777) ||
	die " Could not create fifo \ n " if !( - e $v - >[0]);
	sysopen ( $v - >[2] , $v - >[0] , $v - >[1]| O_NONBLOCK ) ||
	die " Could not open fifo \ n " ;
}
while (1)
{
	sysread ( $h { ' IN '} - >[2] , my $data , 65535);
	last if ( $data =~ m /^\ s *( quit | exit )\ s * $ /);
	syswrite ( $h { ' OUT '} - >[2] , ` $data `);
}
foreach my $v ( values % h )
{
	close $v - >[2];
	unlink $v - >[0];
}
