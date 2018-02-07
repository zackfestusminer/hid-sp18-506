from eve import Eve
import platform
import psutil
app = Eve ()


@app.route("/processor")
def processor():
    return platform.processor()

@app.route("/virtual_memory")
def virtual_memory():
    return str(psutil.virtual_memory().total)

@app.route("/disk_usage")
def disk_usage():
    return str(psutil.disk_usage('/').total)

@app.route("/boot_time")
def boot_time():
	return str(psutil.boot_time())

if __name__ == '__main__':
    app.run()




