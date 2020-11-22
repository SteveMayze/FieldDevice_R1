# Chapter 18 Exercise 2

# Definitions - Serial Input function, preset the number of modules.

# Wait for Ground on Test PIN

# Transmit API packet "ND"

# For each expected module:
    # Wait for 0xFE
    # for each byte received
        # Get message-byte-count bytes - Calculate the byte count
        # Get message data byte - Save byte in dataND array - add checksum bytes
    # End for
    # if checksum not OK
        # Error - Throw exception
# End For
# Done LED on - Print XBee data

