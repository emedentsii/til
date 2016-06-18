To create new docker machine with own insecure registry:

`$ docker-machine create -d virtualbox --engine-insecure-registry your-registry.com docker_test`

Connect to machine:

`$ eval $(docker-machine env docker_test)`

Get machine ip

`docker-machine ip`
