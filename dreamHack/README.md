```
docker buildx build --platform=linux/amd64 -t ubuntu-pwndbg .

alias dhdocker='docker run -it --rm --platform=linux/amd64 -v $(pwd):/app ubuntu-pwndbg'

docker container prune   # 중지된 컨테이너 제거
docker image prune       # dangling 이미지 제거
docker system prune -a   # 미사용 이미지, 컨테이너, 볼륨 전부 제거
```


```
docker buildx build --platform=linux/amd64 -t chall .
docker run -it --rm --platform=linux/amd64 -v $(pwd):/app chall
```
