import psutil
from flask import Flask, render_template

app = Flask(__name__)

# Start home route
@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    disk_metric = psutil.disk_usage('/').percent  # Disk usage
    net_io_metric = psutil.net_io_counters()  # Network I/O statistics
    Message = None
    if cpu_metric > 80 or mem_metric > 80 or disk_metric > 80:
        Message = "High CPU, Memory or Disk usage detected! Please check the applications running or consider scaling up."
    return render_template(
        "index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, disk_metric=disk_metric, net_io_metric=net_io_metric, message=Message
    )

# Main method
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")