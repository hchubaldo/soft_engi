build:
	git pull
	docker build -t ass2 . 

run: build
	docker run -d -p 5000:5000 ass2:latest python ./app.py