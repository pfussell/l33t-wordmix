l33t-wordmix
============
There are a number of tools already out that will create password lists based on a list or rules (hashcat, john), but sometimes these were a bit overkill. 

During pentests I found a need to take target specific accounts for dictionary attacks. In these cases it was helpful to create a password list for that account based on a specific rule (name of the compnay, sports team).

This script will take a single word and create a series of variations on that word based on a set of predefined substitutions. 

