#!/usr/bin/env python
"""This module provides functions for authenticating users."""

def login(username, password):
    """Log the user in."""
    try:
        user_file = open('/etc/users.txt')
        user_buf = user_file.read()
        users = [line.split("|") for line in user_buf.split("\n")]
        return [username, password] in users
    except IOError:
        print "I can't authenticate you."
        return False
def logout():
    print 'You are now logged out.'

def restart():
    print "restart the system?"

def cleanup():
    """this is a fake clean up function"""
    print "clean up the system"

