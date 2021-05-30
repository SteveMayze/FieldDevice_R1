# Base Station

This module represents the code for implemenating a base-station. This is a node of the network that will act as a coordinator to the modules in range. This will maintain a list of the near-by nodes and request data from them from time to time.

# Use Cases

# Node Metadata

# Request Data

# New Node

# Node Removed

# Node Reconnected

# Node Configuration

## TODO
1. The Rest module is not being _injected_. It is not healthy that this is being created down in the Subscriber code.
1. Error handling needs to be consolidated and improved
1. The naming of the class hierarchy is no longer appropriate and should be refactored.
1. There needs to be a protocol devised for the various use cases.
1. The _coordinator_ needs to react and control the protocol.
1. Finalise the payload structure



