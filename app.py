from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index", methods=['POST'])
def move_to_home():
    # logic to create a DNS record
    return render_template("index.html")

@app.route("/create_instance", methods=['POST'])
def create_instance():
    # logic to create a virtual machine
    return render_template('create_instance.html')

@app.route("/create_load_balancer", methods=['POST'])
def create_load_balancer():
    # logic to create a load balancer
    return "Load Balancer created successfully!"

@app.route("/create_dns_record", methods=['POST'])
def create_dns_record():
    # logic to create a DNS record
    return render_template("create_dns_record.html")

@app.route("/resources")
def resources():
    # logic to retrieve user's deployed resources
    resources = [] # replace with actual data
    return render_template('resources.html', resources=resources)

if __name__ == "__main__":
    app.run()
