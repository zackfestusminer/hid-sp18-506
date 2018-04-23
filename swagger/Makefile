service:
	mkdir snp
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i sql-snp-price.yml -l python-flask -o snp -D supportPython3=true
	pip install pymysql
	cp snpPriceFunctions.py snp/
	cp config.py snp/
	cp default_controller.py snp/swagger_server/controllers
	cd snp && pip install -r requirements.txt && python setup.py install


start:
	cd snp && python -m swagger_server

test:
	curl -X PUT "http://localhost:8080/cloudmesh/snp" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"snpDate\": \"2018-04-19\", \"open\": 2701.16, \"high\": 2702.51, \"close\": 2695.99, \"low\": 2692.49, \"adjClose\": 2695.99, \"volume\": 241378247}"
	curl -X PATCH "http://localhost:8080/cloudmesh/snp/2018-04-19" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"snpDate\": \"2017-4-18\", \"open\": 2342.530029, \"high\": 2348.350098, \"close\": 2342.189941, \"low\": 2334.540039, \"adjClose\": 2342.189941, \"volume\": 3269840001}"
	curl -X GET "http://localhost:8080/cloudmesh/snp" -H "accept: application/json"
	curl -X GET "http://localhost:8080/cloudmesh/snp/2018-4-18" -H "accept: application/json"
	curl -X DELETE "http://localhost:8080/cloudmesh/snp/2018-04-19" -H "accept: application/json"

stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	rm -r snp
	rm swagger-codegen-cli.jar
	
container:
	docker build -t cloudmesh-snp-sql .
	docker create cloudmesh-snp-sql

container_start:
	docker run cloudmesh-snp-sql
