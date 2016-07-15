
Remove all images

`docker rmi $(docker images -q)`

Kill containers and remove them:

`docker rm $(docker kill $(docker ps -aq))`

Note: Replace kill with stop for graceful shutdown

Remove all images except "my-image"
You could use grep to remove all except my-image and ubuntu

`docker rmi $(docker images | grep -v 'ubuntu\|my-image' | awk {'print $3'})`

Remove all untagged images

`docker rmi $(docker images -q --filter "dangling=true")`
