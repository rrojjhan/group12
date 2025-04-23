# Group12

## CPE4020: Smart Home Temperature Monitoring System Group 12 ##

# Use-Case Description: 
In this system, a Raspberry Pi SenseHat sensor (publisher) will collect temperature data from a room. This data will be sent to a broker, which will store and forward the temperature data to a subscriber, a desktop, which will display the temperature and alert the user if the temperature exceeds a certain threshold. 

Pub/Sub using Raspberry Pi SenseHat
# Instruction: 
1.	To run the program, you need a VPN so data can be accessed, received, and sent securely within the same private network. To do this, go to https://tailscale.com and download the free program. The program will require the user to create an account.
2.	Once you have created an account, go to the Admin console. Make sure to add the devices used as the publisher, subscriber, and broker.
3.	Once you add all devices used, copy the IP address that is assigned to the device running the Server program. 
4.	Next, download the zip file containing the three Python files. They are named accordingly to be run under the designated device. The only contingency is that the publisher file must be run by the Raspberry Pi. The Subscriber and Broker file can be used by any device that can run Python.
5.	Open all the files and find the line containing HOST= ' ', and paste the Broker IP address that we copied earlier inside the single quote.
6.	Run the Server file so that the broker can be opened to receive/send data. Ideally, run the subscriber before the publisher so the subscriber can receive everything. Have fun!!
