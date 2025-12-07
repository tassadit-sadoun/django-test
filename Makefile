# Start the docker containers
docker-up: ## Start the docker containers
	docker-compose up --build

# Stop the docker containers
docker-down: ## Stop the docker containers
	docker-compose down

# Access the web container shell
docker-sh: ## Access the docker container shell
	docker exec -it padam-web sh
	
dokcer-migrate: ## Apply database migrations inside the container
	docker exec -it padam-web python manage.py migrate

docker

# Create a Django superuser inside the container
docker-superuser: ## Create a superuser for the Django admin
	docker exec -it padam-web python manage.py createsuperuser

# Run the Django dev server inside the container
docker-run: ## Run the test server inside the container
	docker exec -it padam-web python manage.py runserver_plus 0.0.0.0:8000

# Create sample data inside the container
docker-create-data: ## Create sample data
	docker exec -it padam-web python manage.py create_data

# Assign permissions to non-driver users inside the container
docker-assign-perms: ## Make non-driver users staff and assign BusShift & BusStop permissions
	docker exec -it padam-web python manage.py update_non_drivers

# Assign permissions to non-driver users inside the container
docker-user_test: ## 
	docker exec -it padam-web python manage.py create_test_user

# Run tests inside the container
docker-test: ## Run tests inside the container
docker exec -it padam-web python manage.py test

