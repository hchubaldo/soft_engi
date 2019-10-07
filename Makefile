build:
	git pull
	docker stop ass2
	docker build -t ass2 . 

run: build
	docker run -d -p 80:80 --name ass2 ass2:latest python ./app.py