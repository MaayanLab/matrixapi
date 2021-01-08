
docker build -f DockerFile -t maayanlab/matrixapi .
docker push maayanlab/matrixapi

docker kill matrixapi
docker rm matrixapi

#docker run --name matrixapi -e BASE_NAME="matrixapi" -e TOKEN="welcome" -e MATRIX_URL="https://mssm-seq-matrix.s3.amazonaws.com/human_correlation_test.h5" -p 5001:5000 -i maayanlab/matrixapi
