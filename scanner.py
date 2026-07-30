import logging
import socket
from flask import Flask, render_template, request, flash
import threading

app = Flask(__name__)
app.secret_key = 'd3f4c9e23f8g18h2d9d8h3g7h'

#Set up logging to capture scan activities
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')




#Function for scanning single port on given IP
def scan_port(ip,port, result_list):
    try:
	#Creating a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            result_list.append((port, True)) #if connection is successful
        else:
            result_list.append((port, False)) #if connection fails, port is closed
    except Exception as e:
        logging.error(f"Error scanning port {port} on {ip}: {str(e)}") #log any exceptions
        result_list.append((port, False))
    finally:
        sock.close()


#Route to handle form and port scanning
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        ip = request.form.get('ip')
        try:
            socket.inet_aton(ip)
        except socket.error:
            flash("Invalid IP address")
            return render_template("index.html")

        # Check if custom range is selected
        use_custom_range = 'custom_range' in request.form

        if use_custom_range:
            start_port = request.form.get("start_port")
            end_port = request.form.get("end_port")
            
            # If start_port and end_port are empty, set default values
            if not start_port or not end_port:
                flash("Please provide both start and end ports.")
                return render_template('index.html')

            start_port = int(start_port)
            end_port = int(end_port)
        else:
            # Default to 1 to 1000 if custom range is not selected
            start_port = 1
            end_port = 1000
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            flash("Port range must be between 1 and 65535 and start should be less than end.")
            return render_template('index.html')
            

	#Scan ports in given range
        open_ports = []
        threads = []
        result_list = []
	
        for port in range(start_port, end_port +1):
	    #create a new thread for each port scan
            thread = threading.Thread(target=scan_port, args=(ip, port, result_list))
            threads.append(thread)
            thread.start()
	
	#wait for all threads to be done
        for thread in threads:
            thread.join()

	#Filtering open ports
        open_ports = [port for port, is_open in result_list if is_open]

        #log results
        logging.info(f"Open ports for {ip}: {open_ports}")

	#Pass the open open ports to the results page
        return render_template('result.html', ip=ip, open_ports=open_ports)
	
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

