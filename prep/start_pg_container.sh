docker run -d \
	--name vntechies_pg \
	-e POSTGRES_PASSWORD=password_kho_doan \
    -e POSTGRES_USER=vntechies \
    -e POSTGRES_DB=test \
    -p 5432:5432 \
	postgres:9.6