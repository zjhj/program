#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pexpect
import sys

def do_oper( curr_data ):
    # print( curr_data )

    curr_host = curr_data[0]

    curr_user = curr_data[1]
    curr_pswd = curr_data[2]

    curr_root = curr_data[3]

    new_user = curr_data[4]
    new_pswd = curr_data[5]

    child = pexpect.spawn( 'ssh {} -l {}'.format(curr_host,curr_user), timeout=2 )

    try:
        while True:
            index = child.expect( ['password','yes/no','.+\$\s*$',pexpect.EOF,pexpect.TIMEOUT] )
            # print( 'index={}'.format(index) )
            if index == 0:
                child.sendline( curr_pswd )
            elif index == 1:
                child.sendline( 'yes' )
            elif index == 2:
                break
            else:
                return False

        # print( 'switch user' )
        child.sendline( 'su -' )
        index = child.expect( ['[pP]assword',pexpect.EOF,pexpect.TIMEOUT] )
        # print( 'index_su={}'.format(index) )
        if index == 0:
            child.sendline( curr_root )
        else:
            return False

        # print( 'add user' )
        child.sendline( 'adduser {}'.format(new_user) )
        index = child.expect( ['password',pexpect.EOF,pexpect.TIMEOUT] )
        if index == 0:
            child.sendline( new_pswd )
        else:
            return False

        # print( 'password again' )
        index = child.expect( ['new password',pexpect.EOF,pexpect.TIMEOUT] )
        if index == 0:
            child.sendline( new_pswd )
        else:
            return False

        # print( 'fulfill information' )
        n = 6
        while n>0:
            index = child.expect( [']',pexpect.EOF,pexpect.TIMEOUT] )
            if index == 0:
                n -= 1
                child.sendline()
            else:
                return False

        child.sendline( 'exit' )
        child.sendline( 'exit' )

        return True

    except:
        return False

def do_main():
    if len(sys.argv) < 2:
        print( 'Please provide config-file!' )
        return False

    with open(sys.argv[1]) as fp:
        line_data = fp.read().split('\n')

        for curr_line in line_data:
            curr_line = curr_line.strip()
            if len(curr_line) > 0:
                curr_data = curr_line.split(':')
                if len(curr_data) == 6:
                    if do_oper( curr_data ):
                        print( '{}@{} success!'.format(curr_data[4],curr_data[0]) )
                    else:
                        print( '{}@{} failed!'.format(curr_data[4],curr_data[0]) )

if __name__ == '__main__':
    do_main()
