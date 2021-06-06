REGISTRY=harbor.tanzu.bekind.io/demoapps
IMAGE=wholefoodsfrugality
TAG=0.3

pack build ${REGISTRY}/${IMAGE}:${TAG}
docker push ${REGISTRY}/${IMAGE}:${TAG}

docker tag ${REGISTRY}/${IMAGE}:${TAG} ${REGISTRY}/${IMAGE}:latest
docker ${REGISTRY}/${IMAGE}:latest
