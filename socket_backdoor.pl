#!/usr/bin/perl -w

use strict;

use IO::Socket::UNIX;

my $sock = '/tmp/sock';
my $srv = IO::Socket::UNIX->new(Type => SOCK_STREAM(),
                                Local => $sock,
                                Listen => 1);
while (my $cln = $srv->accept())
{
    my $data = <$cln>;
    last if ($data =~ m/^\s*(quit|exit)\s*$/);
    print $cln `$data`;
    close $cln;
}
close $srv;
unlink $sock;