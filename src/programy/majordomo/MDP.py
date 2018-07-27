"""Majordomo Protocol definitions"""
#  This is the version of MDP/Client we implement
C_CLIENT = "MDPC01"

#  This is the version of MDP/Worker we implement
W_WORKER = "MDPW01"

#  MDP/Server commands, as strings
W_READY         =   b"01" 
W_REQUEST       =   b"02" 
W_REPLY         =   b"03" 
W_HEARTBEAT     =   b"04" 
W_DISCONNECT    =   b"05" 

commands = [None, "READY", "REQUEST", "REPLY", "HEARTBEAT", "DISCONNECT"]
